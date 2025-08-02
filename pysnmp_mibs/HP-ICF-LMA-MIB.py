_A8='hpicfLmaConfigGroup3'
_A7='hpicfLmaConfigGroup2'
_A6='hpicfLmaConfigGroup1'
_A5='hpicfLmaSessionStatsGroup'
_A4='hpicfLmaConfigGroup'
_A3='hpicfLmaMacGroup'
_A2='hpicfLmaUnauthVidLLDPNwkPolicy'
_A1='hpicfLmaSessionUserRole'
_A0='hpicfLmaUserRoleAssociationRowStatus'
_z='hpicfLmaAssocActiveProfileName'
_y='hpicfLmaSessionMacAddr'
_x='hpicfLmaUserRoleAssociationMacValue'
_w='hpicfLmaUserRoleAssociationMacType'
_v='hpicfLmaUserRoleAssociationName'
_u='macGrp'
_t='hpicfLmaAssociationMacValue'
_s='hpicfLmaAssociationMacType'
_r='hpicfLmaMacValue'
_q='hpicfLmaMacType'
_p='Counter32'
_o='hpicfLmaMacPin'
_n='hpicfLmaSessionUsrNumberCnt'
_m='hpicfLmaSessionUnauthVid'
_l='hpicfLmaSessionAuthVid'
_k='hpicfLmaSessionStateTime'
_j='hpicfLmaSessionState'
_i='hpicfLmaAssociationRowStatus'
_h='hpicfLmaProfileRowStatus'
_g='hpicfLmaProfileIsAssociated'
_f='hpicfLmaProfileCoS'
_e='hpicfLmaProfileTaggedVids'
_d='hpicfLmaProfileUntaggedVid'
_c='hpicfLmaMacRowStatus'
_b='hpicfLmaMacGrpRowStatus'
_a='hpicfLmaPortNumber'
_Z='hpicfLmaProfileName'
_Y='macOui'
_X='macMask'
_W='macAddress'
_V='hpicfLmaMacGrpName'
_U='TruthValue'
_T='hpicfLmaSessionStatsGroup1'
_S='hpicfLmaMacGroup1'
_R='hpicfLmaAssocActiveMacAddress'
_Q='DisplayString'
_P='OctetString'
_O='hpicfLmaReauthenticate'
_N='hpicfLmaUnAuthPeriod'
_M='hpicfLmaUnauthVid'
_L='hpicfLmaAuthVid'
_K='hpicfLmaLogoffPeriod'
_J='hpicfLmaQuietPeriod'
_I='hpicfLmaClientLimit'
_H='deprecated'
_G='read-only'
_F='read-create'
_E='read-write'
_D='not-accessible'
_C='Integer32'
_B='current'
_A='HP-ICF-LMA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpAutzUserRoleName,=mibBuilder.importSymbols('HP-AUTZ-MIB','HpAutzUserRoleName')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VidList,=mibBuilder.importSymbols('HP-ICF-TC','VidList')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_p,'Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_Q,'MacAddress','PhysAddress','RowStatus','TextualConvention',_U)
hpicfLmaMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97))
if mibBuilder.loadTexts:hpicfLmaMIB.setRevisions(('2018-10-30 00:00','2017-06-28 07:10','2016-02-12 07:10','2013-04-10 09:00'))
_HpicfLmaNotifications_ObjectIdentity=ObjectIdentity
hpicfLmaNotifications=_HpicfLmaNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,0))
_HpicfLmaObjects_ObjectIdentity=ObjectIdentity
hpicfLmaObjects=_HpicfLmaObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,1))
_HpicfLmaConfigObjects_ObjectIdentity=ObjectIdentity
hpicfLmaConfigObjects=_HpicfLmaConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1))
_HpicfLmaScalarObjects_ObjectIdentity=ObjectIdentity
hpicfLmaScalarObjects=_HpicfLmaScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,1))
_HpicfLmaMacGrpTable_Object=MibTable
hpicfLmaMacGrpTable=_HpicfLmaMacGrpTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,2))
if mibBuilder.loadTexts:hpicfLmaMacGrpTable.setStatus(_B)
_HpicfLmaMacGrpEntry_Object=MibTableRow
hpicfLmaMacGrpEntry=_HpicfLmaMacGrpEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,2,1))
hpicfLmaMacGrpEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:hpicfLmaMacGrpEntry.setStatus(_B)
class _HpicfLmaMacGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfLmaMacGrpName_Type.__name__=_Q
_HpicfLmaMacGrpName_Object=MibTableColumn
hpicfLmaMacGrpName=_HpicfLmaMacGrpName_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,2,1,1),_HpicfLmaMacGrpName_Type())
hpicfLmaMacGrpName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaMacGrpName.setStatus(_B)
_HpicfLmaMacGrpRowStatus_Type=RowStatus
_HpicfLmaMacGrpRowStatus_Object=MibTableColumn
hpicfLmaMacGrpRowStatus=_HpicfLmaMacGrpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,2,1,2),_HpicfLmaMacGrpRowStatus_Type())
hpicfLmaMacGrpRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaMacGrpRowStatus.setStatus(_B)
_HpicfLmaMacTable_Object=MibTable
hpicfLmaMacTable=_HpicfLmaMacTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,3))
if mibBuilder.loadTexts:hpicfLmaMacTable.setStatus(_B)
_HpicfLmaMacEntry_Object=MibTableRow
hpicfLmaMacEntry=_HpicfLmaMacEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,3,1))
hpicfLmaMacEntry.setIndexNames((0,_A,_V),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:hpicfLmaMacEntry.setStatus(_B)
class _HpicfLmaMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_HpicfLmaMacType_Type.__name__=_C
_HpicfLmaMacType_Object=MibTableColumn
hpicfLmaMacType=_HpicfLmaMacType_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,3,1,1),_HpicfLmaMacType_Type())
hpicfLmaMacType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaMacType.setStatus(_B)
class _HpicfLmaMacValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,6))
_HpicfLmaMacValue_Type.__name__=_P
_HpicfLmaMacValue_Object=MibTableColumn
hpicfLmaMacValue=_HpicfLmaMacValue_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,3,1,2),_HpicfLmaMacValue_Type())
hpicfLmaMacValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaMacValue.setStatus(_B)
_HpicfLmaMacRowStatus_Type=RowStatus
_HpicfLmaMacRowStatus_Object=MibTableColumn
hpicfLmaMacRowStatus=_HpicfLmaMacRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,3,1,3),_HpicfLmaMacRowStatus_Type())
hpicfLmaMacRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaMacRowStatus.setStatus(_B)
_HpicfLmaProfileTable_Object=MibTable
hpicfLmaProfileTable=_HpicfLmaProfileTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4))
if mibBuilder.loadTexts:hpicfLmaProfileTable.setStatus(_B)
_HpicfLmaProfileEntry_Object=MibTableRow
hpicfLmaProfileEntry=_HpicfLmaProfileEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4,1))
hpicfLmaProfileEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:hpicfLmaProfileEntry.setStatus(_B)
class _HpicfLmaProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfLmaProfileName_Type.__name__=_Q
_HpicfLmaProfileName_Object=MibTableColumn
hpicfLmaProfileName=_HpicfLmaProfileName_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4,1,1),_HpicfLmaProfileName_Type())
hpicfLmaProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaProfileName.setStatus(_B)
class _HpicfLmaProfileUntaggedVid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfLmaProfileUntaggedVid_Type.__name__=_C
_HpicfLmaProfileUntaggedVid_Object=MibTableColumn
hpicfLmaProfileUntaggedVid=_HpicfLmaProfileUntaggedVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4,1,2),_HpicfLmaProfileUntaggedVid_Type())
hpicfLmaProfileUntaggedVid.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaProfileUntaggedVid.setStatus(_B)
_HpicfLmaProfileTaggedVids_Type=VidList
_HpicfLmaProfileTaggedVids_Object=MibTableColumn
hpicfLmaProfileTaggedVids=_HpicfLmaProfileTaggedVids_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4,1,3),_HpicfLmaProfileTaggedVids_Type())
hpicfLmaProfileTaggedVids.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaProfileTaggedVids.setStatus(_B)
class _HpicfLmaProfileCoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_HpicfLmaProfileCoS_Type.__name__=_C
_HpicfLmaProfileCoS_Object=MibTableColumn
hpicfLmaProfileCoS=_HpicfLmaProfileCoS_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4,1,4),_HpicfLmaProfileCoS_Type())
hpicfLmaProfileCoS.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaProfileCoS.setStatus(_B)
_HpicfLmaProfileIsAssociated_Type=TruthValue
_HpicfLmaProfileIsAssociated_Object=MibTableColumn
hpicfLmaProfileIsAssociated=_HpicfLmaProfileIsAssociated_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4,1,5),_HpicfLmaProfileIsAssociated_Type())
hpicfLmaProfileIsAssociated.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaProfileIsAssociated.setStatus(_B)
_HpicfLmaProfileRowStatus_Type=RowStatus
_HpicfLmaProfileRowStatus_Object=MibTableColumn
hpicfLmaProfileRowStatus=_HpicfLmaProfileRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,4,1,6),_HpicfLmaProfileRowStatus_Type())
hpicfLmaProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaProfileRowStatus.setStatus(_B)
_HpicfLmaAssociationTable_Object=MibTable
hpicfLmaAssociationTable=_HpicfLmaAssociationTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,5))
if mibBuilder.loadTexts:hpicfLmaAssociationTable.setStatus(_B)
_HpicfLmaAssociationEntry_Object=MibTableRow
hpicfLmaAssociationEntry=_HpicfLmaAssociationEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,5,1))
hpicfLmaAssociationEntry.setIndexNames((0,_A,_Z),(0,_A,_s),(0,_A,_t))
if mibBuilder.loadTexts:hpicfLmaAssociationEntry.setStatus(_B)
class _HpicfLmaAssociationMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_u,0),(_W,1),(_X,2),(_Y,3)))
_HpicfLmaAssociationMacType_Type.__name__=_C
_HpicfLmaAssociationMacType_Object=MibTableColumn
hpicfLmaAssociationMacType=_HpicfLmaAssociationMacType_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,5,1,2),_HpicfLmaAssociationMacType_Type())
hpicfLmaAssociationMacType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaAssociationMacType.setStatus(_B)
class _HpicfLmaAssociationMacValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfLmaAssociationMacValue_Type.__name__=_P
_HpicfLmaAssociationMacValue_Object=MibTableColumn
hpicfLmaAssociationMacValue=_HpicfLmaAssociationMacValue_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,5,1,4),_HpicfLmaAssociationMacValue_Type())
hpicfLmaAssociationMacValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaAssociationMacValue.setStatus(_B)
_HpicfLmaAssociationRowStatus_Type=RowStatus
_HpicfLmaAssociationRowStatus_Object=MibTableColumn
hpicfLmaAssociationRowStatus=_HpicfLmaAssociationRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,5,1,5),_HpicfLmaAssociationRowStatus_Type())
hpicfLmaAssociationRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaAssociationRowStatus.setStatus(_B)
_HpicfLmaConfigTable_Object=MibTable
hpicfLmaConfigTable=_HpicfLmaConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6))
if mibBuilder.loadTexts:hpicfLmaConfigTable.setStatus(_B)
_HpicfLmaConfigEntry_Object=MibTableRow
hpicfLmaConfigEntry=_HpicfLmaConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1))
hpicfLmaConfigEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:hpicfLmaConfigEntry.setStatus(_B)
_HpicfLmaPortNumber_Type=InterfaceIndex
_HpicfLmaPortNumber_Object=MibTableColumn
hpicfLmaPortNumber=_HpicfLmaPortNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,1),_HpicfLmaPortNumber_Type())
hpicfLmaPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaPortNumber.setStatus(_B)
class _HpicfLmaClientLimit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HpicfLmaClientLimit_Type.__name__=_C
_HpicfLmaClientLimit_Object=MibTableColumn
hpicfLmaClientLimit=_HpicfLmaClientLimit_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,2),_HpicfLmaClientLimit_Type())
hpicfLmaClientLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaClientLimit.setStatus(_B)
class _HpicfLmaQuietPeriod_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfLmaQuietPeriod_Type.__name__=_C
_HpicfLmaQuietPeriod_Object=MibTableColumn
hpicfLmaQuietPeriod=_HpicfLmaQuietPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,4),_HpicfLmaQuietPeriod_Type())
hpicfLmaQuietPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaQuietPeriod.setStatus(_B)
class _HpicfLmaLogoffPeriod_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999999))
_HpicfLmaLogoffPeriod_Type.__name__=_C
_HpicfLmaLogoffPeriod_Object=MibTableColumn
hpicfLmaLogoffPeriod=_HpicfLmaLogoffPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,5),_HpicfLmaLogoffPeriod_Type())
hpicfLmaLogoffPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaLogoffPeriod.setStatus(_B)
class _HpicfLmaAuthVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfLmaAuthVid_Type.__name__=_C
_HpicfLmaAuthVid_Object=MibTableColumn
hpicfLmaAuthVid=_HpicfLmaAuthVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,7),_HpicfLmaAuthVid_Type())
hpicfLmaAuthVid.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaAuthVid.setStatus(_B)
class _HpicfLmaUnauthVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfLmaUnauthVid_Type.__name__=_C
_HpicfLmaUnauthVid_Object=MibTableColumn
hpicfLmaUnauthVid=_HpicfLmaUnauthVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,8),_HpicfLmaUnauthVid_Type())
hpicfLmaUnauthVid.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaUnauthVid.setStatus(_B)
class _HpicfLmaUnAuthPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfLmaUnAuthPeriod_Type.__name__=_C
_HpicfLmaUnAuthPeriod_Object=MibTableColumn
hpicfLmaUnAuthPeriod=_HpicfLmaUnAuthPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,9),_HpicfLmaUnAuthPeriod_Type())
hpicfLmaUnAuthPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaUnAuthPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpicfLmaUnAuthPeriod.setUnits('seconds')
_HpicfLmaReauthenticate_Type=TruthValue
_HpicfLmaReauthenticate_Object=MibTableColumn
hpicfLmaReauthenticate=_HpicfLmaReauthenticate_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,10),_HpicfLmaReauthenticate_Type())
hpicfLmaReauthenticate.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaReauthenticate.setStatus(_B)
class _HpicfLmaMacPin_Type(TruthValue):defaultValue=2
_HpicfLmaMacPin_Type.__name__=_U
_HpicfLmaMacPin_Object=MibTableColumn
hpicfLmaMacPin=_HpicfLmaMacPin_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,11),_HpicfLmaMacPin_Type())
hpicfLmaMacPin.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaMacPin.setStatus(_B)
class _HpicfLmaUnauthVidLLDPNwkPolicy_Type(TruthValue):defaultValue=2
_HpicfLmaUnauthVidLLDPNwkPolicy_Type.__name__=_U
_HpicfLmaUnauthVidLLDPNwkPolicy_Object=MibTableColumn
hpicfLmaUnauthVidLLDPNwkPolicy=_HpicfLmaUnauthVidLLDPNwkPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,6,1,12),_HpicfLmaUnauthVidLLDPNwkPolicy_Type())
hpicfLmaUnauthVidLLDPNwkPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfLmaUnauthVidLLDPNwkPolicy.setStatus(_B)
_HpicfLmaUserRoleAssociationTable_Object=MibTable
hpicfLmaUserRoleAssociationTable=_HpicfLmaUserRoleAssociationTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,7))
if mibBuilder.loadTexts:hpicfLmaUserRoleAssociationTable.setStatus(_B)
_HpicfLmaUserRoleAssociationEntry_Object=MibTableRow
hpicfLmaUserRoleAssociationEntry=_HpicfLmaUserRoleAssociationEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,7,1))
hpicfLmaUserRoleAssociationEntry.setIndexNames((0,_A,_v),(0,_A,_w),(0,_A,_x))
if mibBuilder.loadTexts:hpicfLmaUserRoleAssociationEntry.setStatus(_B)
_HpicfLmaUserRoleAssociationName_Type=HpAutzUserRoleName
_HpicfLmaUserRoleAssociationName_Object=MibTableColumn
hpicfLmaUserRoleAssociationName=_HpicfLmaUserRoleAssociationName_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,7,1,1),_HpicfLmaUserRoleAssociationName_Type())
hpicfLmaUserRoleAssociationName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaUserRoleAssociationName.setStatus(_B)
class _HpicfLmaUserRoleAssociationMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_u,0),(_W,1),(_X,2),(_Y,3)))
_HpicfLmaUserRoleAssociationMacType_Type.__name__=_C
_HpicfLmaUserRoleAssociationMacType_Object=MibTableColumn
hpicfLmaUserRoleAssociationMacType=_HpicfLmaUserRoleAssociationMacType_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,7,1,2),_HpicfLmaUserRoleAssociationMacType_Type())
hpicfLmaUserRoleAssociationMacType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaUserRoleAssociationMacType.setStatus(_B)
class _HpicfLmaUserRoleAssociationMacValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfLmaUserRoleAssociationMacValue_Type.__name__=_P
_HpicfLmaUserRoleAssociationMacValue_Object=MibTableColumn
hpicfLmaUserRoleAssociationMacValue=_HpicfLmaUserRoleAssociationMacValue_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,7,1,3),_HpicfLmaUserRoleAssociationMacValue_Type())
hpicfLmaUserRoleAssociationMacValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaUserRoleAssociationMacValue.setStatus(_B)
_HpicfLmaUserRoleAssociationRowStatus_Type=RowStatus
_HpicfLmaUserRoleAssociationRowStatus_Object=MibTableColumn
hpicfLmaUserRoleAssociationRowStatus=_HpicfLmaUserRoleAssociationRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,1,7,1,4),_HpicfLmaUserRoleAssociationRowStatus_Type())
hpicfLmaUserRoleAssociationRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfLmaUserRoleAssociationRowStatus.setStatus(_B)
_HpicfLmaStatsObjects_ObjectIdentity=ObjectIdentity
hpicfLmaStatsObjects=_HpicfLmaStatsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2))
_HpicfLmaSessionStatsTable_Object=MibTable
hpicfLmaSessionStatsTable=_HpicfLmaSessionStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1))
if mibBuilder.loadTexts:hpicfLmaSessionStatsTable.setStatus(_B)
_HpicfLmaSessionStatsEntry_Object=MibTableRow
hpicfLmaSessionStatsEntry=_HpicfLmaSessionStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1))
hpicfLmaSessionStatsEntry.setIndexNames((0,_A,_a),(0,_A,_y))
if mibBuilder.loadTexts:hpicfLmaSessionStatsEntry.setStatus(_B)
_HpicfLmaSessionMacAddr_Type=MacAddress
_HpicfLmaSessionMacAddr_Object=MibTableColumn
hpicfLmaSessionMacAddr=_HpicfLmaSessionMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1,1),_HpicfLmaSessionMacAddr_Type())
hpicfLmaSessionMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaSessionMacAddr.setStatus(_B)
class _HpicfLmaSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('authenticated',1),('unauthenticated',2),('authenticating',3),('authReqRejectNoVlan',4),('authReqRejectUnauthVlan',5),('authReqTimeoutNoVlan',6),('authReqTimeoutUnauthVlan',7),('initialRole',8),('initialRoleFailed',9)))
_HpicfLmaSessionState_Type.__name__=_C
_HpicfLmaSessionState_Object=MibTableColumn
hpicfLmaSessionState=_HpicfLmaSessionState_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1,2),_HpicfLmaSessionState_Type())
hpicfLmaSessionState.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaSessionState.setStatus(_B)
_HpicfLmaSessionStateTime_Type=Unsigned32
_HpicfLmaSessionStateTime_Object=MibTableColumn
hpicfLmaSessionStateTime=_HpicfLmaSessionStateTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1,3),_HpicfLmaSessionStateTime_Type())
hpicfLmaSessionStateTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaSessionStateTime.setStatus(_B)
class _HpicfLmaSessionAuthVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfLmaSessionAuthVid_Type.__name__=_C
_HpicfLmaSessionAuthVid_Object=MibTableColumn
hpicfLmaSessionAuthVid=_HpicfLmaSessionAuthVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1,4),_HpicfLmaSessionAuthVid_Type())
hpicfLmaSessionAuthVid.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaSessionAuthVid.setStatus(_B)
class _HpicfLmaSessionUnauthVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfLmaSessionUnauthVid_Type.__name__=_C
_HpicfLmaSessionUnauthVid_Object=MibTableColumn
hpicfLmaSessionUnauthVid=_HpicfLmaSessionUnauthVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1,5),_HpicfLmaSessionUnauthVid_Type())
hpicfLmaSessionUnauthVid.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaSessionUnauthVid.setStatus(_B)
class _HpicfLmaSessionUsrNumberCnt_Type(Counter32):defaultValue=0
_HpicfLmaSessionUsrNumberCnt_Type.__name__=_p
_HpicfLmaSessionUsrNumberCnt_Object=MibTableColumn
hpicfLmaSessionUsrNumberCnt=_HpicfLmaSessionUsrNumberCnt_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1,6),_HpicfLmaSessionUsrNumberCnt_Type())
hpicfLmaSessionUsrNumberCnt.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaSessionUsrNumberCnt.setStatus(_B)
_HpicfLmaSessionUserRole_Type=HpAutzUserRoleName
_HpicfLmaSessionUserRole_Object=MibTableColumn
hpicfLmaSessionUserRole=_HpicfLmaSessionUserRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,1,1,7),_HpicfLmaSessionUserRole_Type())
hpicfLmaSessionUserRole.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaSessionUserRole.setStatus(_B)
_HpicfLmaAssocActiveTable_Object=MibTable
hpicfLmaAssocActiveTable=_HpicfLmaAssocActiveTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,2))
if mibBuilder.loadTexts:hpicfLmaAssocActiveTable.setStatus(_B)
_HpicfLmaAssocActiveEntry_Object=MibTableRow
hpicfLmaAssocActiveEntry=_HpicfLmaAssocActiveEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,2,1))
hpicfLmaAssocActiveEntry.setIndexNames((0,_A,_z),(0,_A,_R))
if mibBuilder.loadTexts:hpicfLmaAssocActiveEntry.setStatus(_B)
class _HpicfLmaAssocActiveProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfLmaAssocActiveProfileName_Type.__name__=_Q
_HpicfLmaAssocActiveProfileName_Object=MibTableColumn
hpicfLmaAssocActiveProfileName=_HpicfLmaAssocActiveProfileName_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,2,1,1),_HpicfLmaAssocActiveProfileName_Type())
hpicfLmaAssocActiveProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLmaAssocActiveProfileName.setStatus(_B)
_HpicfLmaAssocActiveMacAddress_Type=MacAddress
_HpicfLmaAssocActiveMacAddress_Object=MibTableColumn
hpicfLmaAssocActiveMacAddress=_HpicfLmaAssocActiveMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,97,1,2,2,1,2),_HpicfLmaAssocActiveMacAddress_Type())
hpicfLmaAssocActiveMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfLmaAssocActiveMacAddress.setStatus(_B)
_HpicfLmaConformance_ObjectIdentity=ObjectIdentity
hpicfLmaConformance=_HpicfLmaConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,2))
_HpicfLmaCompliances_ObjectIdentity=ObjectIdentity
hpicfLmaCompliances=_HpicfLmaCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,2,1))
_HpicfLmaGroups_ObjectIdentity=ObjectIdentity
hpicfLmaGroups=_HpicfLmaGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2))
hpicfLmaMacGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,1))
hpicfLmaMacGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:hpicfLmaMacGroup.setStatus(_H)
hpicfLmaConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,2))
hpicfLmaConfigGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:hpicfLmaConfigGroup.setStatus(_H)
hpicfLmaSessionStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,3))
hpicfLmaSessionStatsGroup.setObjects(*((_A,_R),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:hpicfLmaSessionStatsGroup.setStatus(_H)
hpicfLmaMacGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,4))
hpicfLmaMacGroup1.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_A0)))
if mibBuilder.loadTexts:hpicfLmaMacGroup1.setStatus(_B)
hpicfLmaConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,5))
hpicfLmaConfigGroup1.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:hpicfLmaConfigGroup1.setStatus(_H)
hpicfLmaSessionStatsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,6))
hpicfLmaSessionStatsGroup1.setObjects(*((_A,_R),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_A1)))
if mibBuilder.loadTexts:hpicfLmaSessionStatsGroup1.setStatus(_B)
hpicfLmaConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,7))
hpicfLmaConfigGroup2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_o)))
if mibBuilder.loadTexts:hpicfLmaConfigGroup2.setStatus(_H)
hpicfLmaConfigGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,97,2,2,8))
hpicfLmaConfigGroup3.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_o),(_A,_A2)))
if mibBuilder.loadTexts:hpicfLmaConfigGroup3.setStatus(_B)
hpicfLmaCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,97,2,1,1))
hpicfLmaCompliance1.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:hpicfLmaCompliance1.setStatus(_H)
hpicfLmaCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,97,2,1,2))
hpicfLmaCompliance2.setObjects(*((_A,_S),(_A,_A6),(_A,_T)))
if mibBuilder.loadTexts:hpicfLmaCompliance2.setStatus(_H)
hpicfLmaCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,97,2,1,3))
hpicfLmaCompliance3.setObjects(*((_A,_S),(_A,_A7),(_A,_T)))
if mibBuilder.loadTexts:hpicfLmaCompliance3.setStatus(_H)
hpicfLmaCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,97,2,1,4))
hpicfLmaCompliance4.setObjects(*((_A,_S),(_A,_A8),(_A,_T)))
if mibBuilder.loadTexts:hpicfLmaCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfLmaMIB':hpicfLmaMIB,'hpicfLmaNotifications':hpicfLmaNotifications,'hpicfLmaObjects':hpicfLmaObjects,'hpicfLmaConfigObjects':hpicfLmaConfigObjects,'hpicfLmaScalarObjects':hpicfLmaScalarObjects,'hpicfLmaMacGrpTable':hpicfLmaMacGrpTable,'hpicfLmaMacGrpEntry':hpicfLmaMacGrpEntry,_V:hpicfLmaMacGrpName,_b:hpicfLmaMacGrpRowStatus,'hpicfLmaMacTable':hpicfLmaMacTable,'hpicfLmaMacEntry':hpicfLmaMacEntry,_q:hpicfLmaMacType,_r:hpicfLmaMacValue,_c:hpicfLmaMacRowStatus,'hpicfLmaProfileTable':hpicfLmaProfileTable,'hpicfLmaProfileEntry':hpicfLmaProfileEntry,_Z:hpicfLmaProfileName,_d:hpicfLmaProfileUntaggedVid,_e:hpicfLmaProfileTaggedVids,_f:hpicfLmaProfileCoS,_g:hpicfLmaProfileIsAssociated,_h:hpicfLmaProfileRowStatus,'hpicfLmaAssociationTable':hpicfLmaAssociationTable,'hpicfLmaAssociationEntry':hpicfLmaAssociationEntry,_s:hpicfLmaAssociationMacType,_t:hpicfLmaAssociationMacValue,_i:hpicfLmaAssociationRowStatus,'hpicfLmaConfigTable':hpicfLmaConfigTable,'hpicfLmaConfigEntry':hpicfLmaConfigEntry,_a:hpicfLmaPortNumber,_I:hpicfLmaClientLimit,_J:hpicfLmaQuietPeriod,_K:hpicfLmaLogoffPeriod,_L:hpicfLmaAuthVid,_M:hpicfLmaUnauthVid,_N:hpicfLmaUnAuthPeriod,_O:hpicfLmaReauthenticate,_o:hpicfLmaMacPin,_A2:hpicfLmaUnauthVidLLDPNwkPolicy,'hpicfLmaUserRoleAssociationTable':hpicfLmaUserRoleAssociationTable,'hpicfLmaUserRoleAssociationEntry':hpicfLmaUserRoleAssociationEntry,_v:hpicfLmaUserRoleAssociationName,_w:hpicfLmaUserRoleAssociationMacType,_x:hpicfLmaUserRoleAssociationMacValue,_A0:hpicfLmaUserRoleAssociationRowStatus,'hpicfLmaStatsObjects':hpicfLmaStatsObjects,'hpicfLmaSessionStatsTable':hpicfLmaSessionStatsTable,'hpicfLmaSessionStatsEntry':hpicfLmaSessionStatsEntry,_y:hpicfLmaSessionMacAddr,_j:hpicfLmaSessionState,_k:hpicfLmaSessionStateTime,_l:hpicfLmaSessionAuthVid,_m:hpicfLmaSessionUnauthVid,_n:hpicfLmaSessionUsrNumberCnt,_A1:hpicfLmaSessionUserRole,'hpicfLmaAssocActiveTable':hpicfLmaAssocActiveTable,'hpicfLmaAssocActiveEntry':hpicfLmaAssocActiveEntry,_z:hpicfLmaAssocActiveProfileName,_R:hpicfLmaAssocActiveMacAddress,'hpicfLmaConformance':hpicfLmaConformance,'hpicfLmaCompliances':hpicfLmaCompliances,'hpicfLmaCompliance1':hpicfLmaCompliance1,'hpicfLmaCompliance2':hpicfLmaCompliance2,'hpicfLmaCompliance3':hpicfLmaCompliance3,'hpicfLmaCompliance4':hpicfLmaCompliance4,'hpicfLmaGroups':hpicfLmaGroups,_A3:hpicfLmaMacGroup,_A4:hpicfLmaConfigGroup,_A5:hpicfLmaSessionStatsGroup,_S:hpicfLmaMacGroup1,_A6:hpicfLmaConfigGroup1,_T:hpicfLmaSessionStatsGroup1,_A7:hpicfLmaConfigGroup2,_A8:hpicfLmaConfigGroup3})