_A9='lecsMIBGroup'
_A8='lecsLesConfigStatus'
_A7='lecsLesConnState'
_A6='lecsLesPriority'
_A5='lecsConfigDirectDstType'
_A4='lecsMasterState'
_A3='lecsRDConfigStatus'
_A2='lecsRDConfigLastUsed'
_A1='lecsRDConfigElanName'
_A0='lecsElanSegmentId'
_z='lecsElanAccess'
_y='lecsConfigTblDefaultElanName'
_x='lecsConfigDirectConnVCType'
_w='lecsAtmAddrConfigStatus'
_v='lecsAtmAddrLastUsed'
_u='lecsAtmAddrConfigElanName'
_t='lecsMacConfigStatus'
_s='lecsMacConfigLastUsed'
_r='lecsMacConfigElanName'
_q='lecsElanConfigStatus'
_p='lecsElanLesAtmAddr'
_o='lecsConfigTblStatus'
_n='lecsConfigDirectConnDst'
_m='lecsConfigDirectConnSrc'
_l='lecsAtmAddrStatus'
_k='lecsAtmAddrState'
_j='lecsAtmAddrActual'
_i='lecsAtmAddrMask'
_h='lecsAtmAddrSpec'
_g='lecsStatus'
_f='lecsAdminStatus'
_e='lecsOperStatus'
_d='lecsLastFailLec'
_c='lecsLastFailCause'
_b='lecsOutConfigFails'
_a='lecsInConfigErrors'
_Z='lecsInConfigReqs'
_Y='lecsUpTime'
_X='lecsConfigTableName'
_W='lecsRDConfigBridgeNum'
_V='lecsRDConfigSegmentId'
_U='lecsLesAtmAddr'
_T='lecsAtmAddrConfigMask'
_S='lecsAtmAddrConfigAddress'
_R='lecsMacConfigAddress'
_Q='lecsConfigDirectConnVci'
_P='lecsConfigDirectConnVpi'
_O='lecsAtmAddrIndex'
_N='lecsElanConfigName'
_M='inactive'
_L='active'
_K='ifIndex'
_J='IF-MIB'
_I='OctetString'
_H='lecsConfigTblName'
_G='DisplayString'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='CISCO-LECS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_J,_K)
AtmLaneAddress,VciInteger,VpiInteger=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB','AtmLaneAddress','VciInteger','VpiInteger')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoLecsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,38))
_CiscoLecsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLecsMIBObjects=_CiscoLecsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,38,1))
_Lecs_ObjectIdentity=ObjectIdentity
lecs=_Lecs_ObjectIdentity((1,3,6,1,4,1,9,9,38,1,1))
_LecsTable_Object=MibTable
lecsTable=_LecsTable_Object((1,3,6,1,4,1,9,9,38,1,1,1))
if mibBuilder.loadTexts:lecsTable.setStatus(_A)
_LecsEntry_Object=MibTableRow
lecsEntry=_LecsEntry_Object((1,3,6,1,4,1,9,9,38,1,1,1,1))
lecsEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:lecsEntry.setStatus(_A)
class _LecsConfigTableName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LecsConfigTableName_Type.__name__=_G
_LecsConfigTableName_Object=MibTableColumn
lecsConfigTableName=_LecsConfigTableName_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,1),_LecsConfigTableName_Type())
lecsConfigTableName.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsConfigTableName.setStatus(_A)
_LecsUpTime_Type=TimeStamp
_LecsUpTime_Object=MibTableColumn
lecsUpTime=_LecsUpTime_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,2),_LecsUpTime_Type())
lecsUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsUpTime.setStatus(_A)
_LecsInConfigReqs_Type=Counter32
_LecsInConfigReqs_Object=MibTableColumn
lecsInConfigReqs=_LecsInConfigReqs_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,3),_LecsInConfigReqs_Type())
lecsInConfigReqs.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsInConfigReqs.setStatus(_A)
_LecsInConfigErrors_Type=Counter32
_LecsInConfigErrors_Object=MibTableColumn
lecsInConfigErrors=_LecsInConfigErrors_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,4),_LecsInConfigErrors_Type())
lecsInConfigErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsInConfigErrors.setStatus(_A)
_LecsOutConfigFails_Type=Counter32
_LecsOutConfigFails_Object=MibTableColumn
lecsOutConfigFails=_LecsOutConfigFails_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,5),_LecsOutConfigFails_Type())
lecsOutConfigFails.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsOutConfigFails.setStatus(_A)
_LecsLastFailCause_Type=Integer32
_LecsLastFailCause_Object=MibTableColumn
lecsLastFailCause=_LecsLastFailCause_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,6),_LecsLastFailCause_Type())
lecsLastFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsLastFailCause.setStatus(_A)
_LecsLastFailLec_Type=AtmLaneAddress
_LecsLastFailLec_Object=MibTableColumn
lecsLastFailLec=_LecsLastFailLec_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,7),_LecsLastFailLec_Type())
lecsLastFailLec.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsLastFailLec.setStatus(_A)
class _LecsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_LecsOperStatus_Type.__name__=_E
_LecsOperStatus_Object=MibTableColumn
lecsOperStatus=_LecsOperStatus_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,8),_LecsOperStatus_Type())
lecsOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsOperStatus.setStatus(_A)
class _LecsAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_LecsAdminStatus_Type.__name__=_E
_LecsAdminStatus_Object=MibTableColumn
lecsAdminStatus=_LecsAdminStatus_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,9),_LecsAdminStatus_Type())
lecsAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAdminStatus.setStatus(_A)
_LecsStatus_Type=RowStatus
_LecsStatus_Object=MibTableColumn
lecsStatus=_LecsStatus_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,10),_LecsStatus_Type())
lecsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsStatus.setStatus(_A)
_LecsMasterState_Type=TruthValue
_LecsMasterState_Object=MibTableColumn
lecsMasterState=_LecsMasterState_Object((1,3,6,1,4,1,9,9,38,1,1,1,1,11),_LecsMasterState_Type())
lecsMasterState.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsMasterState.setStatus(_A)
_LecsAtmAddrTable_Object=MibTable
lecsAtmAddrTable=_LecsAtmAddrTable_Object((1,3,6,1,4,1,9,9,38,1,1,2))
if mibBuilder.loadTexts:lecsAtmAddrTable.setStatus(_A)
_LecsAtmAddrEntry_Object=MibTableRow
lecsAtmAddrEntry=_LecsAtmAddrEntry_Object((1,3,6,1,4,1,9,9,38,1,1,2,1))
lecsAtmAddrEntry.setIndexNames((0,_J,_K),(0,_B,_O))
if mibBuilder.loadTexts:lecsAtmAddrEntry.setStatus(_A)
class _LecsAtmAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LecsAtmAddrIndex_Type.__name__=_E
_LecsAtmAddrIndex_Object=MibTableColumn
lecsAtmAddrIndex=_LecsAtmAddrIndex_Object((1,3,6,1,4,1,9,9,38,1,1,2,1,1),_LecsAtmAddrIndex_Type())
lecsAtmAddrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsAtmAddrIndex.setStatus(_A)
_LecsAtmAddrSpec_Type=AtmLaneAddress
_LecsAtmAddrSpec_Object=MibTableColumn
lecsAtmAddrSpec=_LecsAtmAddrSpec_Object((1,3,6,1,4,1,9,9,38,1,1,2,1,2),_LecsAtmAddrSpec_Type())
lecsAtmAddrSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmAddrSpec.setStatus(_A)
class _LecsAtmAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_LecsAtmAddrMask_Type.__name__=_I
_LecsAtmAddrMask_Object=MibTableColumn
lecsAtmAddrMask=_LecsAtmAddrMask_Object((1,3,6,1,4,1,9,9,38,1,1,2,1,3),_LecsAtmAddrMask_Type())
lecsAtmAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmAddrMask.setStatus(_A)
_LecsAtmAddrActual_Type=AtmLaneAddress
_LecsAtmAddrActual_Object=MibTableColumn
lecsAtmAddrActual=_LecsAtmAddrActual_Object((1,3,6,1,4,1,9,9,38,1,1,2,1,4),_LecsAtmAddrActual_Type())
lecsAtmAddrActual.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsAtmAddrActual.setStatus(_A)
class _LecsAtmAddrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('actualValueInvalid',1),('actualValueValid',2),('registeredWithSignalling',3),('regSigAndValid',4),('registeredWithIlmi',5),('regIlmiAndValid',6),('regSigandIlmi',7),('regSigIlmiAndValid',8)))
_LecsAtmAddrState_Type.__name__=_E
_LecsAtmAddrState_Object=MibTableColumn
lecsAtmAddrState=_LecsAtmAddrState_Object((1,3,6,1,4,1,9,9,38,1,1,2,1,5),_LecsAtmAddrState_Type())
lecsAtmAddrState.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsAtmAddrState.setStatus(_A)
_LecsAtmAddrStatus_Type=RowStatus
_LecsAtmAddrStatus_Object=MibTableColumn
lecsAtmAddrStatus=_LecsAtmAddrStatus_Object((1,3,6,1,4,1,9,9,38,1,1,2,1,6),_LecsAtmAddrStatus_Type())
lecsAtmAddrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmAddrStatus.setStatus(_A)
_LecsConfigDirectConnTable_Object=MibTable
lecsConfigDirectConnTable=_LecsConfigDirectConnTable_Object((1,3,6,1,4,1,9,9,38,1,1,3))
if mibBuilder.loadTexts:lecsConfigDirectConnTable.setStatus(_A)
_LecsConfigDirectConnEntry_Object=MibTableRow
lecsConfigDirectConnEntry=_LecsConfigDirectConnEntry_Object((1,3,6,1,4,1,9,9,38,1,1,3,1))
lecsConfigDirectConnEntry.setIndexNames((0,_J,_K),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:lecsConfigDirectConnEntry.setStatus(_A)
_LecsConfigDirectConnVpi_Type=VpiInteger
_LecsConfigDirectConnVpi_Object=MibTableColumn
lecsConfigDirectConnVpi=_LecsConfigDirectConnVpi_Object((1,3,6,1,4,1,9,9,38,1,1,3,1,1),_LecsConfigDirectConnVpi_Type())
lecsConfigDirectConnVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsConfigDirectConnVpi.setStatus(_A)
_LecsConfigDirectConnVci_Type=VciInteger
_LecsConfigDirectConnVci_Object=MibTableColumn
lecsConfigDirectConnVci=_LecsConfigDirectConnVci_Object((1,3,6,1,4,1,9,9,38,1,1,3,1,2),_LecsConfigDirectConnVci_Type())
lecsConfigDirectConnVci.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsConfigDirectConnVci.setStatus(_A)
class _LecsConfigDirectConnVCType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pvc',1),('svc',2)))
_LecsConfigDirectConnVCType_Type.__name__=_E
_LecsConfigDirectConnVCType_Object=MibTableColumn
lecsConfigDirectConnVCType=_LecsConfigDirectConnVCType_Object((1,3,6,1,4,1,9,9,38,1,1,3,1,3),_LecsConfigDirectConnVCType_Type())
lecsConfigDirectConnVCType.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsConfigDirectConnVCType.setStatus(_A)
_LecsConfigDirectConnSrc_Type=AtmLaneAddress
_LecsConfigDirectConnSrc_Object=MibTableColumn
lecsConfigDirectConnSrc=_LecsConfigDirectConnSrc_Object((1,3,6,1,4,1,9,9,38,1,1,3,1,4),_LecsConfigDirectConnSrc_Type())
lecsConfigDirectConnSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsConfigDirectConnSrc.setStatus(_A)
_LecsConfigDirectConnDst_Type=AtmLaneAddress
_LecsConfigDirectConnDst_Object=MibTableColumn
lecsConfigDirectConnDst=_LecsConfigDirectConnDst_Object((1,3,6,1,4,1,9,9,38,1,1,3,1,5),_LecsConfigDirectConnDst_Type())
lecsConfigDirectConnDst.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsConfigDirectConnDst.setStatus(_A)
class _LecsConfigDirectDstType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('laneClient',1),('laneServer',2),('laneConfig',3),('unknown',4)))
_LecsConfigDirectDstType_Type.__name__=_E
_LecsConfigDirectDstType_Object=MibTableColumn
lecsConfigDirectDstType=_LecsConfigDirectDstType_Object((1,3,6,1,4,1,9,9,38,1,1,3,1,6),_LecsConfigDirectDstType_Type())
lecsConfigDirectDstType.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsConfigDirectDstType.setStatus(_A)
_Config_ObjectIdentity=ObjectIdentity
config=_Config_ObjectIdentity((1,3,6,1,4,1,9,9,38,1,2))
_LecsConfigTblTable_Object=MibTable
lecsConfigTblTable=_LecsConfigTblTable_Object((1,3,6,1,4,1,9,9,38,1,2,1))
if mibBuilder.loadTexts:lecsConfigTblTable.setStatus(_A)
_LecsConfigTblEntry_Object=MibTableRow
lecsConfigTblEntry=_LecsConfigTblEntry_Object((1,3,6,1,4,1,9,9,38,1,2,1,1))
lecsConfigTblEntry.setIndexNames((1,_B,_H))
if mibBuilder.loadTexts:lecsConfigTblEntry.setStatus(_A)
class _LecsConfigTblName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LecsConfigTblName_Type.__name__=_G
_LecsConfigTblName_Object=MibTableColumn
lecsConfigTblName=_LecsConfigTblName_Object((1,3,6,1,4,1,9,9,38,1,2,1,1,1),_LecsConfigTblName_Type())
lecsConfigTblName.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsConfigTblName.setStatus(_A)
class _LecsConfigTblDefaultElanName_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LecsConfigTblDefaultElanName_Type.__name__=_G
_LecsConfigTblDefaultElanName_Object=MibTableColumn
lecsConfigTblDefaultElanName=_LecsConfigTblDefaultElanName_Object((1,3,6,1,4,1,9,9,38,1,2,1,1,2),_LecsConfigTblDefaultElanName_Type())
lecsConfigTblDefaultElanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsConfigTblDefaultElanName.setStatus(_A)
_LecsConfigTblStatus_Type=RowStatus
_LecsConfigTblStatus_Object=MibTableColumn
lecsConfigTblStatus=_LecsConfigTblStatus_Object((1,3,6,1,4,1,9,9,38,1,2,1,1,3),_LecsConfigTblStatus_Type())
lecsConfigTblStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsConfigTblStatus.setStatus(_A)
_LecsElanConfigTable_Object=MibTable
lecsElanConfigTable=_LecsElanConfigTable_Object((1,3,6,1,4,1,9,9,38,1,2,2))
if mibBuilder.loadTexts:lecsElanConfigTable.setStatus(_A)
_LecsElanConfigEntry_Object=MibTableRow
lecsElanConfigEntry=_LecsElanConfigEntry_Object((1,3,6,1,4,1,9,9,38,1,2,2,1))
lecsElanConfigEntry.setIndexNames((0,_B,_H),(1,_B,_N))
if mibBuilder.loadTexts:lecsElanConfigEntry.setStatus(_A)
class _LecsElanConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LecsElanConfigName_Type.__name__=_G
_LecsElanConfigName_Object=MibTableColumn
lecsElanConfigName=_LecsElanConfigName_Object((1,3,6,1,4,1,9,9,38,1,2,2,1,1),_LecsElanConfigName_Type())
lecsElanConfigName.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsElanConfigName.setStatus(_A)
_LecsElanLesAtmAddr_Type=AtmLaneAddress
_LecsElanLesAtmAddr_Object=MibTableColumn
lecsElanLesAtmAddr=_LecsElanLesAtmAddr_Object((1,3,6,1,4,1,9,9,38,1,2,2,1,2),_LecsElanLesAtmAddr_Type())
lecsElanLesAtmAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsElanLesAtmAddr.setStatus(_A)
class _LecsElanAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('closed',2)))
_LecsElanAccess_Type.__name__=_E
_LecsElanAccess_Object=MibTableColumn
lecsElanAccess=_LecsElanAccess_Object((1,3,6,1,4,1,9,9,38,1,2,2,1,3),_LecsElanAccess_Type())
lecsElanAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsElanAccess.setStatus(_A)
_LecsElanConfigStatus_Type=RowStatus
_LecsElanConfigStatus_Object=MibTableColumn
lecsElanConfigStatus=_LecsElanConfigStatus_Object((1,3,6,1,4,1,9,9,38,1,2,2,1,4),_LecsElanConfigStatus_Type())
lecsElanConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsElanConfigStatus.setStatus(_A)
class _LecsElanSegmentId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LecsElanSegmentId_Type.__name__=_E
_LecsElanSegmentId_Object=MibTableColumn
lecsElanSegmentId=_LecsElanSegmentId_Object((1,3,6,1,4,1,9,9,38,1,2,2,1,5),_LecsElanSegmentId_Type())
lecsElanSegmentId.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsElanSegmentId.setStatus(_A)
_LecsMacConfigTable_Object=MibTable
lecsMacConfigTable=_LecsMacConfigTable_Object((1,3,6,1,4,1,9,9,38,1,2,3))
if mibBuilder.loadTexts:lecsMacConfigTable.setStatus(_A)
_LecsMacConfigEntry_Object=MibTableRow
lecsMacConfigEntry=_LecsMacConfigEntry_Object((1,3,6,1,4,1,9,9,38,1,2,3,1))
lecsMacConfigEntry.setIndexNames((0,_B,_H),(0,_B,_R))
if mibBuilder.loadTexts:lecsMacConfigEntry.setStatus(_A)
_LecsMacConfigAddress_Type=MacAddress
_LecsMacConfigAddress_Object=MibTableColumn
lecsMacConfigAddress=_LecsMacConfigAddress_Object((1,3,6,1,4,1,9,9,38,1,2,3,1,1),_LecsMacConfigAddress_Type())
lecsMacConfigAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsMacConfigAddress.setStatus(_A)
class _LecsMacConfigElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LecsMacConfigElanName_Type.__name__=_G
_LecsMacConfigElanName_Object=MibTableColumn
lecsMacConfigElanName=_LecsMacConfigElanName_Object((1,3,6,1,4,1,9,9,38,1,2,3,1,2),_LecsMacConfigElanName_Type())
lecsMacConfigElanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsMacConfigElanName.setStatus(_A)
_LecsMacConfigLastUsed_Type=TimeStamp
_LecsMacConfigLastUsed_Object=MibTableColumn
lecsMacConfigLastUsed=_LecsMacConfigLastUsed_Object((1,3,6,1,4,1,9,9,38,1,2,3,1,3),_LecsMacConfigLastUsed_Type())
lecsMacConfigLastUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsMacConfigLastUsed.setStatus(_A)
_LecsMacConfigStatus_Type=RowStatus
_LecsMacConfigStatus_Object=MibTableColumn
lecsMacConfigStatus=_LecsMacConfigStatus_Object((1,3,6,1,4,1,9,9,38,1,2,3,1,4),_LecsMacConfigStatus_Type())
lecsMacConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsMacConfigStatus.setStatus(_A)
_LecsAtmAddrConfigTable_Object=MibTable
lecsAtmAddrConfigTable=_LecsAtmAddrConfigTable_Object((1,3,6,1,4,1,9,9,38,1,2,4))
if mibBuilder.loadTexts:lecsAtmAddrConfigTable.setStatus(_A)
_LecsAtmAddrConfigEntry_Object=MibTableRow
lecsAtmAddrConfigEntry=_LecsAtmAddrConfigEntry_Object((1,3,6,1,4,1,9,9,38,1,2,4,1))
lecsAtmAddrConfigEntry.setIndexNames((0,_B,_H),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:lecsAtmAddrConfigEntry.setStatus(_A)
class _LecsAtmAddrConfigAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_LecsAtmAddrConfigAddress_Type.__name__=_I
_LecsAtmAddrConfigAddress_Object=MibTableColumn
lecsAtmAddrConfigAddress=_LecsAtmAddrConfigAddress_Object((1,3,6,1,4,1,9,9,38,1,2,4,1,1),_LecsAtmAddrConfigAddress_Type())
lecsAtmAddrConfigAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsAtmAddrConfigAddress.setStatus(_A)
class _LecsAtmAddrConfigMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_LecsAtmAddrConfigMask_Type.__name__=_I
_LecsAtmAddrConfigMask_Object=MibTableColumn
lecsAtmAddrConfigMask=_LecsAtmAddrConfigMask_Object((1,3,6,1,4,1,9,9,38,1,2,4,1,2),_LecsAtmAddrConfigMask_Type())
lecsAtmAddrConfigMask.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsAtmAddrConfigMask.setStatus(_A)
class _LecsAtmAddrConfigElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LecsAtmAddrConfigElanName_Type.__name__=_G
_LecsAtmAddrConfigElanName_Object=MibTableColumn
lecsAtmAddrConfigElanName=_LecsAtmAddrConfigElanName_Object((1,3,6,1,4,1,9,9,38,1,2,4,1,3),_LecsAtmAddrConfigElanName_Type())
lecsAtmAddrConfigElanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmAddrConfigElanName.setStatus(_A)
_LecsAtmAddrLastUsed_Type=TimeStamp
_LecsAtmAddrLastUsed_Object=MibTableColumn
lecsAtmAddrLastUsed=_LecsAtmAddrLastUsed_Object((1,3,6,1,4,1,9,9,38,1,2,4,1,4),_LecsAtmAddrLastUsed_Type())
lecsAtmAddrLastUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsAtmAddrLastUsed.setStatus(_A)
_LecsAtmAddrConfigStatus_Type=RowStatus
_LecsAtmAddrConfigStatus_Object=MibTableColumn
lecsAtmAddrConfigStatus=_LecsAtmAddrConfigStatus_Object((1,3,6,1,4,1,9,9,38,1,2,4,1,5),_LecsAtmAddrConfigStatus_Type())
lecsAtmAddrConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsAtmAddrConfigStatus.setStatus(_A)
_LecsLesConfigTable_Object=MibTable
lecsLesConfigTable=_LecsLesConfigTable_Object((1,3,6,1,4,1,9,9,38,1,2,5))
if mibBuilder.loadTexts:lecsLesConfigTable.setStatus(_A)
_LecsLesConfigEntry_Object=MibTableRow
lecsLesConfigEntry=_LecsLesConfigEntry_Object((1,3,6,1,4,1,9,9,38,1,2,5,1))
lecsLesConfigEntry.setIndexNames((0,_B,_H),(0,_B,_N),(0,_B,_U))
if mibBuilder.loadTexts:lecsLesConfigEntry.setStatus(_A)
class _LecsLesAtmAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_LecsLesAtmAddr_Type.__name__=_I
_LecsLesAtmAddr_Object=MibTableColumn
lecsLesAtmAddr=_LecsLesAtmAddr_Object((1,3,6,1,4,1,9,9,38,1,2,5,1,1),_LecsLesAtmAddr_Type())
lecsLesAtmAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsLesAtmAddr.setStatus(_A)
class _LecsLesPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_LecsLesPriority_Type.__name__=_E
_LecsLesPriority_Object=MibTableColumn
lecsLesPriority=_LecsLesPriority_Object((1,3,6,1,4,1,9,9,38,1,2,5,1,2),_LecsLesPriority_Type())
lecsLesPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsLesPriority.setStatus(_A)
class _LecsLesConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('notConnected',3)))
_LecsLesConnState_Type.__name__=_E
_LecsLesConnState_Object=MibTableColumn
lecsLesConnState=_LecsLesConnState_Object((1,3,6,1,4,1,9,9,38,1,2,5,1,3),_LecsLesConnState_Type())
lecsLesConnState.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsLesConnState.setStatus(_A)
_LecsLesConfigStatus_Type=RowStatus
_LecsLesConfigStatus_Object=MibTableColumn
lecsLesConfigStatus=_LecsLesConfigStatus_Object((1,3,6,1,4,1,9,9,38,1,2,5,1,4),_LecsLesConfigStatus_Type())
lecsLesConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsLesConfigStatus.setStatus(_A)
_LecsRDConfigTable_Object=MibTable
lecsRDConfigTable=_LecsRDConfigTable_Object((1,3,6,1,4,1,9,9,38,1,2,6))
if mibBuilder.loadTexts:lecsRDConfigTable.setStatus(_A)
_LecsRDConfigEntry_Object=MibTableRow
lecsRDConfigEntry=_LecsRDConfigEntry_Object((1,3,6,1,4,1,9,9,38,1,2,6,1))
lecsRDConfigEntry.setIndexNames((0,_B,_H),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:lecsRDConfigEntry.setStatus(_A)
class _LecsRDConfigSegmentId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LecsRDConfigSegmentId_Type.__name__=_E
_LecsRDConfigSegmentId_Object=MibTableColumn
lecsRDConfigSegmentId=_LecsRDConfigSegmentId_Object((1,3,6,1,4,1,9,9,38,1,2,6,1,1),_LecsRDConfigSegmentId_Type())
lecsRDConfigSegmentId.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsRDConfigSegmentId.setStatus(_A)
class _LecsRDConfigBridgeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LecsRDConfigBridgeNum_Type.__name__=_E
_LecsRDConfigBridgeNum_Object=MibTableColumn
lecsRDConfigBridgeNum=_LecsRDConfigBridgeNum_Object((1,3,6,1,4,1,9,9,38,1,2,6,1,2),_LecsRDConfigBridgeNum_Type())
lecsRDConfigBridgeNum.setMaxAccess(_F)
if mibBuilder.loadTexts:lecsRDConfigBridgeNum.setStatus(_A)
class _LecsRDConfigElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LecsRDConfigElanName_Type.__name__=_G
_LecsRDConfigElanName_Object=MibTableColumn
lecsRDConfigElanName=_LecsRDConfigElanName_Object((1,3,6,1,4,1,9,9,38,1,2,6,1,3),_LecsRDConfigElanName_Type())
lecsRDConfigElanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsRDConfigElanName.setStatus(_A)
_LecsRDConfigLastUsed_Type=TimeStamp
_LecsRDConfigLastUsed_Object=MibTableColumn
lecsRDConfigLastUsed=_LecsRDConfigLastUsed_Object((1,3,6,1,4,1,9,9,38,1,2,6,1,4),_LecsRDConfigLastUsed_Type())
lecsRDConfigLastUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:lecsRDConfigLastUsed.setStatus(_A)
_LecsRDConfigStatus_Type=RowStatus
_LecsRDConfigStatus_Object=MibTableColumn
lecsRDConfigStatus=_LecsRDConfigStatus_Object((1,3,6,1,4,1,9,9,38,1,2,6,1,5),_LecsRDConfigStatus_Type())
lecsRDConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lecsRDConfigStatus.setStatus(_A)
_LecsMIBConformance_ObjectIdentity=ObjectIdentity
lecsMIBConformance=_LecsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,38,2))
_LecsMIBCompliances_ObjectIdentity=ObjectIdentity
lecsMIBCompliances=_LecsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,38,2,1))
_LecsMIBGroups_ObjectIdentity=ObjectIdentity
lecsMIBGroups=_LecsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,38,2,2))
lecsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,38,2,2,1))
lecsMIBGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:lecsMIBGroup.setStatus(_A)
lecsTokenRingMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,38,2,2,2))
lecsTokenRingMIBGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:lecsTokenRingMIBGroup.setStatus(_A)
lecsRedundancyMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,38,2,2,3))
lecsRedundancyMIBGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:lecsRedundancyMIBGroup.setStatus(_A)
lecsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,38,2,1,1))
lecsMIBCompliance.setObjects((_B,_A9))
if mibBuilder.loadTexts:lecsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLecsMIB':ciscoLecsMIB,'ciscoLecsMIBObjects':ciscoLecsMIBObjects,'lecs':lecs,'lecsTable':lecsTable,'lecsEntry':lecsEntry,_X:lecsConfigTableName,_Y:lecsUpTime,_Z:lecsInConfigReqs,_a:lecsInConfigErrors,_b:lecsOutConfigFails,_c:lecsLastFailCause,_d:lecsLastFailLec,_e:lecsOperStatus,_f:lecsAdminStatus,_g:lecsStatus,_A4:lecsMasterState,'lecsAtmAddrTable':lecsAtmAddrTable,'lecsAtmAddrEntry':lecsAtmAddrEntry,_O:lecsAtmAddrIndex,_h:lecsAtmAddrSpec,_i:lecsAtmAddrMask,_j:lecsAtmAddrActual,_k:lecsAtmAddrState,_l:lecsAtmAddrStatus,'lecsConfigDirectConnTable':lecsConfigDirectConnTable,'lecsConfigDirectConnEntry':lecsConfigDirectConnEntry,_P:lecsConfigDirectConnVpi,_Q:lecsConfigDirectConnVci,_x:lecsConfigDirectConnVCType,_m:lecsConfigDirectConnSrc,_n:lecsConfigDirectConnDst,_A5:lecsConfigDirectDstType,'config':config,'lecsConfigTblTable':lecsConfigTblTable,'lecsConfigTblEntry':lecsConfigTblEntry,_H:lecsConfigTblName,_y:lecsConfigTblDefaultElanName,_o:lecsConfigTblStatus,'lecsElanConfigTable':lecsElanConfigTable,'lecsElanConfigEntry':lecsElanConfigEntry,_N:lecsElanConfigName,_p:lecsElanLesAtmAddr,_z:lecsElanAccess,_q:lecsElanConfigStatus,_A0:lecsElanSegmentId,'lecsMacConfigTable':lecsMacConfigTable,'lecsMacConfigEntry':lecsMacConfigEntry,_R:lecsMacConfigAddress,_r:lecsMacConfigElanName,_s:lecsMacConfigLastUsed,_t:lecsMacConfigStatus,'lecsAtmAddrConfigTable':lecsAtmAddrConfigTable,'lecsAtmAddrConfigEntry':lecsAtmAddrConfigEntry,_S:lecsAtmAddrConfigAddress,_T:lecsAtmAddrConfigMask,_u:lecsAtmAddrConfigElanName,_v:lecsAtmAddrLastUsed,_w:lecsAtmAddrConfigStatus,'lecsLesConfigTable':lecsLesConfigTable,'lecsLesConfigEntry':lecsLesConfigEntry,_U:lecsLesAtmAddr,_A6:lecsLesPriority,_A7:lecsLesConnState,_A8:lecsLesConfigStatus,'lecsRDConfigTable':lecsRDConfigTable,'lecsRDConfigEntry':lecsRDConfigEntry,_V:lecsRDConfigSegmentId,_W:lecsRDConfigBridgeNum,_A1:lecsRDConfigElanName,_A2:lecsRDConfigLastUsed,_A3:lecsRDConfigStatus,'lecsMIBConformance':lecsMIBConformance,'lecsMIBCompliances':lecsMIBCompliances,'lecsMIBCompliance':lecsMIBCompliance,'lecsMIBGroups':lecsMIBGroups,_A9:lecsMIBGroup,'lecsTokenRingMIBGroup':lecsTokenRingMIBGroup,'lecsRedundancyMIBGroup':lecsRedundancyMIBGroup})