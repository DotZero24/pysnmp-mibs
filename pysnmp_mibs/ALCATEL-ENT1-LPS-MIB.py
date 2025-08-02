_AG='learnedPortSecurityTrapsObjGroup'
_AF='learnedPortSecurityTrapsGroup'
_AE='learnedPortSecurityGlobGroup'
_AD='learnedPortSecurityGroup'
_AC='lpsPortUpAfterLearningWindowExpiredTrap'
_AB='lpsViolationTrap'
_AA='lpsAgL2MacAddressRowStatus'
_A9='lpsL2MacAddressRowStatus'
_A8='lpsAgL2MacAddressLearnType'
_A7='lpsL2MacAddressLearnType'
_A6='lpsLearningWindowPseudoMacMove'
_A5='lpsLearningWindowLearnAsStatic'
_A4='lpsLearningWindowTimeRemaining'
_A3='lpsLearningWindowBootupStatus'
_A2='lpsLearningWindowNoAging'
_A1='lpsConvertToStatic'
_A0='lpsLearningWindowTimeWithStaticConversion'
_z='lpsLearningWindowTime'
_y='lpsViolatingMac'
_x='lpsLearnTrapThreshold'
_w='lpsMaxFilteredMacNum'
_v='lpsRelease'
_u='lpsRowStatus'
_t='lpsOperStatus'
_s='lpsAdminStatus'
_r='lpsHiMacRange'
_q='lpsLoMacRange'
_p='lpsMaxMacNum'
_o='lpsViolationOption'
_n='lpsAgL2VlanId'
_m='lpsAgL2MacAddress'
_l='deprecated'
_k='quarantined'
_j='filtered'
_i='dynamic'
_h='configured'
_g='lpsL2MacAddress'
_f='lpsL2VlanId'
_e='locked'
_d='000000000000'
_c='discard'
_b='shutdown'
_a='restrict'
_Z='SnmpAdminString'
_Y='lpsLearnMac'
_X='lpsTrapBridgeMac'
_W='lpsTrapViolationType'
_V='lpsTrapViolatingMac'
_U='lpsTrapSwitchIpAddr'
_T='lpsTrapIfIndex'
_S='lpsTrapSwitchVlan'
_R='not-accessible'
_Q='MacAddress'
_P='ifIndex'
_O='IF-MIB'
_N='systemServicesTime'
_M='systemServicesDate'
_L='lpsTrapSwitchPort'
_K='lpsTrapSwitchSlice'
_J='lpsTrapSwitchName'
_I='disable'
_H='enable'
_G='read-write'
_F='ALCATEL-ENT1-SYSTEM-MIB'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='current'
_A='ALCATEL-ENT1-LPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1MacAddress,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1MacAddress')
systemServicesDate,systemServicesTime=mibBuilder.importSymbols(_F,_M,_N)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_O,'InterfaceIndex',_P)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Z)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_Q,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1LearnedPortSecurityMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIB.setRevisions(('2010-05-13 00:00','2007-04-03 00:00'))
_AlcatelIND1LearnedPortSecurityMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBNotifications=_AlcatelIND1LearnedPortSecurityMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2,0))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBNotifications.setStatus(_B)
_AlcatelIND1LearnedPortSecurityMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBObjects=_AlcatelIND1LearnedPortSecurityMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2,1))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBObjects.setStatus(_B)
_LearnedPortSecurityTable_Object=MibTable
learnedPortSecurityTable=_LearnedPortSecurityTable_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1))
if mibBuilder.loadTexts:learnedPortSecurityTable.setStatus(_B)
_LearnedPortSecurityEntry_Object=MibTableRow
learnedPortSecurityEntry=_LearnedPortSecurityEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1))
learnedPortSecurityEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:learnedPortSecurityEntry.setStatus(_B)
class _LpsViolationOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3)))
_LpsViolationOption_Type.__name__=_C
_LpsViolationOption_Object=MibTableColumn
lpsViolationOption=_LpsViolationOption_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,1),_LpsViolationOption_Type())
lpsViolationOption.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsViolationOption.setStatus(_B)
class _LpsMaxMacNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_LpsMaxMacNum_Type.__name__=_C
_LpsMaxMacNum_Object=MibTableColumn
lpsMaxMacNum=_LpsMaxMacNum_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,2),_LpsMaxMacNum_Type())
lpsMaxMacNum.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsMaxMacNum.setStatus(_B)
class _LpsLoMacRange_Type(MacAddress):defaultHexValue=_d
_LpsLoMacRange_Type.__name__=_Q
_LpsLoMacRange_Object=MibTableColumn
lpsLoMacRange=_LpsLoMacRange_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,3),_LpsLoMacRange_Type())
lpsLoMacRange.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsLoMacRange.setStatus(_B)
class _LpsHiMacRange_Type(MacAddress):defaultHexValue='ffffffffffff'
_LpsHiMacRange_Type.__name__=_Q
_LpsHiMacRange_Object=MibTableColumn
lpsHiMacRange=_LpsHiMacRange_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,4),_LpsHiMacRange_Type())
lpsHiMacRange.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsHiMacRange.setStatus(_B)
class _LpsAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),(_e,3)))
_LpsAdminStatus_Type.__name__=_C
_LpsAdminStatus_Object=MibTableColumn
lpsAdminStatus=_LpsAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,5),_LpsAdminStatus_Type())
lpsAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsAdminStatus.setStatus(_B)
class _LpsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('securityViolated',3),(_e,4)))
_LpsOperStatus_Type.__name__=_C
_LpsOperStatus_Object=MibTableColumn
lpsOperStatus=_LpsOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,6),_LpsOperStatus_Type())
lpsOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsOperStatus.setStatus(_B)
_LpsRowStatus_Type=RowStatus
_LpsRowStatus_Object=MibTableColumn
lpsRowStatus=_LpsRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,7),_LpsRowStatus_Type())
lpsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsRowStatus.setStatus(_B)
class _LpsRelease_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('release',1))
_LpsRelease_Type.__name__=_C
_LpsRelease_Object=MibTableColumn
lpsRelease=_LpsRelease_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,8),_LpsRelease_Type())
lpsRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsRelease.setStatus(_B)
class _LpsMaxFilteredMacNum_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LpsMaxFilteredMacNum_Type.__name__=_C
_LpsMaxFilteredMacNum_Object=MibTableColumn
lpsMaxFilteredMacNum=_LpsMaxFilteredMacNum_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,9),_LpsMaxFilteredMacNum_Type())
lpsMaxFilteredMacNum.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsMaxFilteredMacNum.setStatus(_B)
class _LpsLearnTrapThreshold_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_LpsLearnTrapThreshold_Type.__name__=_C
_LpsLearnTrapThreshold_Object=MibTableColumn
lpsLearnTrapThreshold=_LpsLearnTrapThreshold_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,10),_LpsLearnTrapThreshold_Type())
lpsLearnTrapThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsLearnTrapThreshold.setStatus(_B)
class _LpsViolatingMac_Type(MacAddress):defaultHexValue=_d
_LpsViolatingMac_Type.__name__=_Q
_LpsViolatingMac_Object=MibTableColumn
lpsViolatingMac=_LpsViolatingMac_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,1,1,11),_LpsViolatingMac_Type())
lpsViolatingMac.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsViolatingMac.setStatus(_B)
_LearnedPortSecurityGlobalGroup_ObjectIdentity=ObjectIdentity
learnedPortSecurityGlobalGroup=_LearnedPortSecurityGlobalGroup_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3))
class _LpsLearningWindowTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2880))
_LpsLearningWindowTime_Type.__name__=_C
_LpsLearningWindowTime_Object=MibScalar
lpsLearningWindowTime=_LpsLearningWindowTime_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,1),_LpsLearningWindowTime_Type())
lpsLearningWindowTime.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowTime.setStatus(_B)
class _LpsLearningWindowTimeWithStaticConversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_LpsLearningWindowTimeWithStaticConversion_Type.__name__=_C
_LpsLearningWindowTimeWithStaticConversion_Object=MibScalar
lpsLearningWindowTimeWithStaticConversion=_LpsLearningWindowTimeWithStaticConversion_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,2),_LpsLearningWindowTimeWithStaticConversion_Type())
lpsLearningWindowTimeWithStaticConversion.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowTimeWithStaticConversion.setStatus(_B)
class _LpsConvertToStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2147483647,2147483647),ValueRangeConstraint(1001,17000))
_LpsConvertToStatic_Type.__name__=_C
_LpsConvertToStatic_Object=MibScalar
lpsConvertToStatic=_LpsConvertToStatic_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,3),_LpsConvertToStatic_Type())
lpsConvertToStatic.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsConvertToStatic.setStatus(_B)
class _LpsLearningWindowNoAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_LpsLearningWindowNoAging_Type.__name__=_C
_LpsLearningWindowNoAging_Object=MibScalar
lpsLearningWindowNoAging=_LpsLearningWindowNoAging_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,4),_LpsLearningWindowNoAging_Type())
lpsLearningWindowNoAging.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowNoAging.setStatus(_B)
class _LpsLearningWindowBootupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_LpsLearningWindowBootupStatus_Type.__name__=_C
_LpsLearningWindowBootupStatus_Object=MibScalar
lpsLearningWindowBootupStatus=_LpsLearningWindowBootupStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,5),_LpsLearningWindowBootupStatus_Type())
lpsLearningWindowBootupStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowBootupStatus.setStatus(_B)
class _LpsLearningWindowTimeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,172800))
_LpsLearningWindowTimeRemaining_Type.__name__=_C
_LpsLearningWindowTimeRemaining_Object=MibScalar
lpsLearningWindowTimeRemaining=_LpsLearningWindowTimeRemaining_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,6),_LpsLearningWindowTimeRemaining_Type())
lpsLearningWindowTimeRemaining.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsLearningWindowTimeRemaining.setStatus(_B)
class _LpsLearningWindowLearnAsStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_LpsLearningWindowLearnAsStatic_Type.__name__=_C
_LpsLearningWindowLearnAsStatic_Object=MibScalar
lpsLearningWindowLearnAsStatic=_LpsLearningWindowLearnAsStatic_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,7),_LpsLearningWindowLearnAsStatic_Type())
lpsLearningWindowLearnAsStatic.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowLearnAsStatic.setStatus(_B)
class _LpsLearningWindowPseudoMacMove_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_LpsLearningWindowPseudoMacMove_Type.__name__=_C
_LpsLearningWindowPseudoMacMove_Object=MibScalar
lpsLearningWindowPseudoMacMove=_LpsLearningWindowPseudoMacMove_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,3,8),_LpsLearningWindowPseudoMacMove_Type())
lpsLearningWindowPseudoMacMove.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowPseudoMacMove.setStatus(_B)
_LearnedPortSecurityL2MacAddressTable_Object=MibTable
learnedPortSecurityL2MacAddressTable=_LearnedPortSecurityL2MacAddressTable_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,4))
if mibBuilder.loadTexts:learnedPortSecurityL2MacAddressTable.setStatus(_B)
_LearnedPortSecurityL2MacAddressEntry_Object=MibTableRow
learnedPortSecurityL2MacAddressEntry=_LearnedPortSecurityL2MacAddressEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,4,1))
learnedPortSecurityL2MacAddressEntry.setIndexNames((0,_O,_P),(0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:learnedPortSecurityL2MacAddressEntry.setStatus(_B)
class _LpsL2VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_LpsL2VlanId_Type.__name__=_C
_LpsL2VlanId_Object=MibTableColumn
lpsL2VlanId=_LpsL2VlanId_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,4,1,1),_LpsL2VlanId_Type())
lpsL2VlanId.setMaxAccess(_R)
if mibBuilder.loadTexts:lpsL2VlanId.setStatus(_B)
_LpsL2MacAddress_Type=MacAddress
_LpsL2MacAddress_Object=MibTableColumn
lpsL2MacAddress=_LpsL2MacAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,4,1,2),_LpsL2MacAddress_Type())
lpsL2MacAddress.setMaxAccess(_R)
if mibBuilder.loadTexts:lpsL2MacAddress.setStatus(_B)
class _LpsL2MacAddressLearnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4)))
_LpsL2MacAddressLearnType_Type.__name__=_C
_LpsL2MacAddressLearnType_Object=MibTableColumn
lpsL2MacAddressLearnType=_LpsL2MacAddressLearnType_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,4,1,3),_LpsL2MacAddressLearnType_Type())
lpsL2MacAddressLearnType.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsL2MacAddressLearnType.setStatus(_B)
_LpsL2MacAddressRowStatus_Type=RowStatus
_LpsL2MacAddressRowStatus_Object=MibTableColumn
lpsL2MacAddressRowStatus=_LpsL2MacAddressRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,4,1,4),_LpsL2MacAddressRowStatus_Type())
lpsL2MacAddressRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsL2MacAddressRowStatus.setStatus(_B)
_LpsTrapsObj_ObjectIdentity=ObjectIdentity
lpsTrapsObj=_LpsTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5))
class _LpsTrapSwitchName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_LpsTrapSwitchName_Type.__name__=_Z
_LpsTrapSwitchName_Object=MibScalar
lpsTrapSwitchName=_LpsTrapSwitchName_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,1),_LpsTrapSwitchName_Type())
lpsTrapSwitchName.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapSwitchName.setStatus(_B)
_LpsTrapSwitchIpAddr_Type=IpAddress
_LpsTrapSwitchIpAddr_Object=MibScalar
lpsTrapSwitchIpAddr=_LpsTrapSwitchIpAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,2),_LpsTrapSwitchIpAddr_Type())
lpsTrapSwitchIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapSwitchIpAddr.setStatus(_B)
_LpsTrapSwitchSlice_Type=Integer32
_LpsTrapSwitchSlice_Object=MibScalar
lpsTrapSwitchSlice=_LpsTrapSwitchSlice_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,3),_LpsTrapSwitchSlice_Type())
lpsTrapSwitchSlice.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapSwitchSlice.setStatus(_l)
_LpsTrapSwitchPort_Type=Integer32
_LpsTrapSwitchPort_Object=MibScalar
lpsTrapSwitchPort=_LpsTrapSwitchPort_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,4),_LpsTrapSwitchPort_Type())
lpsTrapSwitchPort.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapSwitchPort.setStatus(_l)
_LpsTrapViolatingMac_Type=MacAddress
_LpsTrapViolatingMac_Object=MibScalar
lpsTrapViolatingMac=_LpsTrapViolatingMac_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,5),_LpsTrapViolatingMac_Type())
lpsTrapViolatingMac.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapViolatingMac.setStatus(_B)
class _LpsTrapViolationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3)))
_LpsTrapViolationType_Type.__name__=_C
_LpsTrapViolationType_Object=MibScalar
lpsTrapViolationType=_LpsTrapViolationType_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,6),_LpsTrapViolationType_Type())
lpsTrapViolationType.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapViolationType.setStatus(_B)
_LpsTrapSwitchVlan_Type=Integer32
_LpsTrapSwitchVlan_Object=MibScalar
lpsTrapSwitchVlan=_LpsTrapSwitchVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,7),_LpsTrapSwitchVlan_Type())
lpsTrapSwitchVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapSwitchVlan.setStatus(_B)
_LpsTrapBridgeMac_Type=MacAddress
_LpsTrapBridgeMac_Object=MibScalar
lpsTrapBridgeMac=_LpsTrapBridgeMac_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,8),_LpsTrapBridgeMac_Type())
lpsTrapBridgeMac.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapBridgeMac.setStatus(_B)
_LpsTrapIfIndex_Type=InterfaceIndex
_LpsTrapIfIndex_Object=MibScalar
lpsTrapIfIndex=_LpsTrapIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,5,9),_LpsTrapIfIndex_Type())
lpsTrapIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsTrapIfIndex.setStatus(_B)
_LearnedPortSecurityAgL2MacAddressTable_Object=MibTable
learnedPortSecurityAgL2MacAddressTable=_LearnedPortSecurityAgL2MacAddressTable_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,6))
if mibBuilder.loadTexts:learnedPortSecurityAgL2MacAddressTable.setStatus(_B)
_LearnedPortSecurityAgL2MacAddressEntry_Object=MibTableRow
learnedPortSecurityAgL2MacAddressEntry=_LearnedPortSecurityAgL2MacAddressEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,6,1))
learnedPortSecurityAgL2MacAddressEntry.setIndexNames((0,_O,_P),(0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:learnedPortSecurityAgL2MacAddressEntry.setStatus(_B)
_LpsAgL2MacAddress_Type=MacAddress
_LpsAgL2MacAddress_Object=MibTableColumn
lpsAgL2MacAddress=_LpsAgL2MacAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,6,1,1),_LpsAgL2MacAddress_Type())
lpsAgL2MacAddress.setMaxAccess(_R)
if mibBuilder.loadTexts:lpsAgL2MacAddress.setStatus(_B)
class _LpsAgL2VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_LpsAgL2VlanId_Type.__name__=_C
_LpsAgL2VlanId_Object=MibTableColumn
lpsAgL2VlanId=_LpsAgL2VlanId_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,6,1,2),_LpsAgL2VlanId_Type())
lpsAgL2VlanId.setMaxAccess(_R)
if mibBuilder.loadTexts:lpsAgL2VlanId.setStatus(_B)
class _LpsAgL2MacAddressLearnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4),('configuredFiltered',5),('pseudoStatic',6)))
_LpsAgL2MacAddressLearnType_Type.__name__=_C
_LpsAgL2MacAddressLearnType_Object=MibTableColumn
lpsAgL2MacAddressLearnType=_LpsAgL2MacAddressLearnType_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,6,1,3),_LpsAgL2MacAddressLearnType_Type())
lpsAgL2MacAddressLearnType.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsAgL2MacAddressLearnType.setStatus(_B)
_LpsAgL2MacAddressRowStatus_Type=RowStatus
_LpsAgL2MacAddressRowStatus_Object=MibTableColumn
lpsAgL2MacAddressRowStatus=_LpsAgL2MacAddressRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,8,2,1,6,1,4),_LpsAgL2MacAddressRowStatus_Type())
lpsAgL2MacAddressRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsAgL2MacAddressRowStatus.setStatus(_B)
_AlcatelIND1LearnedPortSecurityMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBConformance=_AlcatelIND1LearnedPortSecurityMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2,2))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBConformance.setStatus(_B)
_AlcatelIND1LearnedPortSecurityMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBGroups=_AlcatelIND1LearnedPortSecurityMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,1))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBGroups.setStatus(_B)
_AlcatelIND1LearnedPortSecurityMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBCompliances=_AlcatelIND1LearnedPortSecurityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,2))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBCompliances.setStatus(_B)
learnedPortSecurityGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,1,1))
learnedPortSecurityGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:learnedPortSecurityGroup.setStatus(_B)
learnedPortSecurityGlobGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,1,2))
learnedPortSecurityGlobGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:learnedPortSecurityGlobGroup.setStatus(_B)
learnedPortSecurityL2MacAddressGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,1,4))
learnedPortSecurityL2MacAddressGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:learnedPortSecurityL2MacAddressGroup.setStatus(_B)
learnedPortSecurityTrapsObjGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,1,6))
learnedPortSecurityTrapsObjGroup.setObjects(*((_A,_J),(_A,_U),(_A,_K),(_A,_L),(_A,_V),(_A,_W),(_A,_S),(_A,_X),(_A,_T)))
if mibBuilder.loadTexts:learnedPortSecurityTrapsObjGroup.setStatus(_B)
lpsViolationTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,8,2,0,1))
lpsViolationTrap.setObjects(*((_A,_J),(_A,_U),(_A,_K),(_A,_L),(_A,_V),(_A,_W),(_A,_S),(_F,_M),(_F,_N),(_A,_T)))
if mibBuilder.loadTexts:lpsViolationTrap.setStatus(_B)
lpsPortUpAfterLearningWindowExpiredTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,8,2,0,2))
lpsPortUpAfterLearningWindowExpiredTrap.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_F,_M),(_F,_N)))
if mibBuilder.loadTexts:lpsPortUpAfterLearningWindowExpiredTrap.setStatus(_B)
lpsLearnMac=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,8,2,0,3))
lpsLearnMac.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_S),(_A,_X),(_F,_M),(_F,_N),(_A,_T)))
if mibBuilder.loadTexts:lpsLearnMac.setStatus(_B)
learnedPortSecurityTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,1,3))
learnedPortSecurityTrapsGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_Y)))
if mibBuilder.loadTexts:learnedPortSecurityTrapsGroup.setStatus(_B)
learnedPortSecurityNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,1,7))
learnedPortSecurityNotificationGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:learnedPortSecurityNotificationGroup.setStatus(_B)
alcatelIND1LearnedPortSecurityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,8,2,2,2,1))
alcatelIND1LearnedPortSecurityMIBCompliance.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1LearnedPortSecurityMIB':alcatelIND1LearnedPortSecurityMIB,'alcatelIND1LearnedPortSecurityMIBNotifications':alcatelIND1LearnedPortSecurityMIBNotifications,_AB:lpsViolationTrap,_AC:lpsPortUpAfterLearningWindowExpiredTrap,_Y:lpsLearnMac,'alcatelIND1LearnedPortSecurityMIBObjects':alcatelIND1LearnedPortSecurityMIBObjects,'learnedPortSecurityTable':learnedPortSecurityTable,'learnedPortSecurityEntry':learnedPortSecurityEntry,_o:lpsViolationOption,_p:lpsMaxMacNum,_q:lpsLoMacRange,_r:lpsHiMacRange,_s:lpsAdminStatus,_t:lpsOperStatus,_u:lpsRowStatus,_v:lpsRelease,_w:lpsMaxFilteredMacNum,_x:lpsLearnTrapThreshold,_y:lpsViolatingMac,'learnedPortSecurityGlobalGroup':learnedPortSecurityGlobalGroup,_z:lpsLearningWindowTime,_A0:lpsLearningWindowTimeWithStaticConversion,_A1:lpsConvertToStatic,_A2:lpsLearningWindowNoAging,_A3:lpsLearningWindowBootupStatus,_A4:lpsLearningWindowTimeRemaining,_A5:lpsLearningWindowLearnAsStatic,_A6:lpsLearningWindowPseudoMacMove,'learnedPortSecurityL2MacAddressTable':learnedPortSecurityL2MacAddressTable,'learnedPortSecurityL2MacAddressEntry':learnedPortSecurityL2MacAddressEntry,_f:lpsL2VlanId,_g:lpsL2MacAddress,_A7:lpsL2MacAddressLearnType,_A9:lpsL2MacAddressRowStatus,'lpsTrapsObj':lpsTrapsObj,_J:lpsTrapSwitchName,_U:lpsTrapSwitchIpAddr,_K:lpsTrapSwitchSlice,_L:lpsTrapSwitchPort,_V:lpsTrapViolatingMac,_W:lpsTrapViolationType,_S:lpsTrapSwitchVlan,_X:lpsTrapBridgeMac,_T:lpsTrapIfIndex,'learnedPortSecurityAgL2MacAddressTable':learnedPortSecurityAgL2MacAddressTable,'learnedPortSecurityAgL2MacAddressEntry':learnedPortSecurityAgL2MacAddressEntry,_m:lpsAgL2MacAddress,_n:lpsAgL2VlanId,_A8:lpsAgL2MacAddressLearnType,_AA:lpsAgL2MacAddressRowStatus,'alcatelIND1LearnedPortSecurityMIBConformance':alcatelIND1LearnedPortSecurityMIBConformance,'alcatelIND1LearnedPortSecurityMIBGroups':alcatelIND1LearnedPortSecurityMIBGroups,_AD:learnedPortSecurityGroup,_AE:learnedPortSecurityGlobGroup,_AF:learnedPortSecurityTrapsGroup,'learnedPortSecurityL2MacAddressGroup':learnedPortSecurityL2MacAddressGroup,_AG:learnedPortSecurityTrapsObjGroup,'learnedPortSecurityNotificationGroup':learnedPortSecurityNotificationGroup,'alcatelIND1LearnedPortSecurityMIBCompliances':alcatelIND1LearnedPortSecurityMIBCompliances,'alcatelIND1LearnedPortSecurityMIBCompliance':alcatelIND1LearnedPortSecurityMIBCompliance})