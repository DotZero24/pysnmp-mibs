_r='trapNotifGroup'
_q='trapTrapsGroup'
_p='trapMgtGroup'
_o='trapAbsorptionTrap'
_n='alaTrapInetFilterStatus'
_m='alaTrapInetStationNextSeq'
_l='alaTrapInetStationReplay'
_k='alaTrapInetStationUser'
_j='alaTrapInetStationProtocol'
_i='alaTrapInetStationRowStatus'
_h='alaTrapInetStationPort'
_g='trapToWebView'
_f='trapAbsorption'
_e='trapFilterStatus'
_d='trapStationNextSeq'
_c='trapStationReplay'
_b='trapStationUser'
_a='trapStationProtocol'
_Z='trapStationRowStatus'
_Y='trapStationPort'
_X='trapAbsorbPeriod'
_W='trapFamily'
_V='trapName'
_U='not-accessible'
_T='disable'
_S='enable'
_R='InetAddress'
_Q='trapAbsorTime'
_P='trapAbsorCounter'
_O='trapAbsorTrapId'
_N='trapAbsorStamp'
_M='alaTrapInetStationIP'
_L='alaTrapInetStationIPType'
_K='accessible-for-notify'
_J='read-write'
_I='trapStationIP'
_H='trapIndex'
_G='DisplayString'
_F='read-only'
_E='Unsigned32'
_D='read-create'
_C='Integer32'
_B='ALCATEL-IND1-TRAP-MGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1TrapMgr,trapMgrTraps=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1TrapMgr','trapMgrTraps')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_R,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1TrapMgrMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,2,1))
if mibBuilder.loadTexts:alcatelIND1TrapMgrMIB.setRevisions(('2007-08-07 00:00',))
_AlcatelIND1TrapMgrMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1TrapMgrMIBObjects=_AlcatelIND1TrapMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,2,1,1))
if mibBuilder.loadTexts:alcatelIND1TrapMgrMIBObjects.setStatus(_A)
_TrapMgt_ObjectIdentity=ObjectIdentity
trapMgt=_TrapMgt_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1))
_TrapConfigTable_Object=MibTable
trapConfigTable=_TrapConfigTable_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,1))
if mibBuilder.loadTexts:trapConfigTable.setStatus(_A)
_TrapConfigEntry_Object=MibTableRow
trapConfigEntry=_TrapConfigEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,1,1))
trapConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:trapConfigEntry.setStatus(_A)
class _TrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_TrapIndex_Type.__name__=_C
_TrapIndex_Object=MibTableColumn
trapIndex=_TrapIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,1,1,1),_TrapIndex_Type())
trapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:trapIndex.setStatus(_A)
class _TrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_TrapName_Type.__name__=_G
_TrapName_Object=MibTableColumn
trapName=_TrapName_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,1,1,2),_TrapName_Type())
trapName.setMaxAccess(_F)
if mibBuilder.loadTexts:trapName.setStatus(_A)
class _TrapFamily_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_TrapFamily_Type.__name__=_G
_TrapFamily_Object=MibTableColumn
trapFamily=_TrapFamily_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,1,1,3),_TrapFamily_Type())
trapFamily.setMaxAccess(_F)
if mibBuilder.loadTexts:trapFamily.setStatus(_A)
class _TrapAbsorbPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_TrapAbsorbPeriod_Type.__name__=_C
_TrapAbsorbPeriod_Object=MibTableColumn
trapAbsorbPeriod=_TrapAbsorbPeriod_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,1,1,4),_TrapAbsorbPeriod_Type())
trapAbsorbPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:trapAbsorbPeriod.setStatus(_A)
_TrapStationTable_Object=MibTable
trapStationTable=_TrapStationTable_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2))
if mibBuilder.loadTexts:trapStationTable.setStatus(_A)
_TrapStationEntry_Object=MibTableRow
trapStationEntry=_TrapStationEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1))
trapStationEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:trapStationEntry.setStatus(_A)
_TrapStationIP_Type=IpAddress
_TrapStationIP_Object=MibTableColumn
trapStationIP=_TrapStationIP_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1,1),_TrapStationIP_Type())
trapStationIP.setMaxAccess(_F)
if mibBuilder.loadTexts:trapStationIP.setStatus(_A)
class _TrapStationPort_Type(Unsigned32):defaultValue=162
_TrapStationPort_Type.__name__=_E
_TrapStationPort_Object=MibTableColumn
trapStationPort=_TrapStationPort_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1,2),_TrapStationPort_Type())
trapStationPort.setMaxAccess(_D)
if mibBuilder.loadTexts:trapStationPort.setStatus(_A)
_TrapStationRowStatus_Type=RowStatus
_TrapStationRowStatus_Object=MibTableColumn
trapStationRowStatus=_TrapStationRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1,3),_TrapStationRowStatus_Type())
trapStationRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:trapStationRowStatus.setStatus(_A)
class _TrapStationProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3)))
_TrapStationProtocol_Type.__name__=_C
_TrapStationProtocol_Object=MibTableColumn
trapStationProtocol=_TrapStationProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1,4),_TrapStationProtocol_Type())
trapStationProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:trapStationProtocol.setStatus(_A)
class _TrapStationUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TrapStationUser_Type.__name__=_G
_TrapStationUser_Object=MibTableColumn
trapStationUser=_TrapStationUser_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1,5),_TrapStationUser_Type())
trapStationUser.setMaxAccess(_D)
if mibBuilder.loadTexts:trapStationUser.setStatus(_A)
class _TrapStationReplay_Type(Unsigned32):defaultValue=0
_TrapStationReplay_Type.__name__=_E
_TrapStationReplay_Object=MibTableColumn
trapStationReplay=_TrapStationReplay_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1,6),_TrapStationReplay_Type())
trapStationReplay.setMaxAccess(_D)
if mibBuilder.loadTexts:trapStationReplay.setStatus(_A)
class _TrapStationNextSeq_Type(Unsigned32):defaultValue=0
_TrapStationNextSeq_Type.__name__=_E
_TrapStationNextSeq_Object=MibTableColumn
trapStationNextSeq=_TrapStationNextSeq_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,2,1,7),_TrapStationNextSeq_Type())
trapStationNextSeq.setMaxAccess(_F)
if mibBuilder.loadTexts:trapStationNextSeq.setStatus(_A)
_TrapFilterTable_Object=MibTable
trapFilterTable=_TrapFilterTable_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,3))
if mibBuilder.loadTexts:trapFilterTable.setStatus(_A)
_TrapFilterEntry_Object=MibTableRow
trapFilterEntry=_TrapFilterEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,3,1))
trapFilterEntry.setIndexNames((0,_B,_I),(0,_B,_H))
if mibBuilder.loadTexts:trapFilterEntry.setStatus(_A)
class _TrapFilterStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_TrapFilterStatus_Type.__name__=_C
_TrapFilterStatus_Object=MibTableColumn
trapFilterStatus=_TrapFilterStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,3,1,1),_TrapFilterStatus_Type())
trapFilterStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:trapFilterStatus.setStatus(_A)
class _TrapAbsorption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_TrapAbsorption_Type.__name__=_C
_TrapAbsorption_Object=MibScalar
trapAbsorption=_TrapAbsorption_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,4),_TrapAbsorption_Type())
trapAbsorption.setMaxAccess(_J)
if mibBuilder.loadTexts:trapAbsorption.setStatus(_A)
class _TrapToWebView_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_TrapToWebView_Type.__name__=_C
_TrapToWebView_Object=MibScalar
trapToWebView=_TrapToWebView_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,5),_TrapToWebView_Type())
trapToWebView.setMaxAccess(_J)
if mibBuilder.loadTexts:trapToWebView.setStatus(_A)
_AlaTrapInetStationTable_Object=MibTable
alaTrapInetStationTable=_AlaTrapInetStationTable_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6))
if mibBuilder.loadTexts:alaTrapInetStationTable.setStatus(_A)
_AlaTrapInetStationEntry_Object=MibTableRow
alaTrapInetStationEntry=_AlaTrapInetStationEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1))
alaTrapInetStationEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:alaTrapInetStationEntry.setStatus(_A)
_AlaTrapInetStationIPType_Type=InetAddressType
_AlaTrapInetStationIPType_Object=MibTableColumn
alaTrapInetStationIPType=_AlaTrapInetStationIPType_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,1),_AlaTrapInetStationIPType_Type())
alaTrapInetStationIPType.setMaxAccess(_U)
if mibBuilder.loadTexts:alaTrapInetStationIPType.setStatus(_A)
class _AlaTrapInetStationIP_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaTrapInetStationIP_Type.__name__=_R
_AlaTrapInetStationIP_Object=MibTableColumn
alaTrapInetStationIP=_AlaTrapInetStationIP_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,2),_AlaTrapInetStationIP_Type())
alaTrapInetStationIP.setMaxAccess(_U)
if mibBuilder.loadTexts:alaTrapInetStationIP.setStatus(_A)
class _AlaTrapInetStationPort_Type(Unsigned32):defaultValue=162
_AlaTrapInetStationPort_Type.__name__=_E
_AlaTrapInetStationPort_Object=MibTableColumn
alaTrapInetStationPort=_AlaTrapInetStationPort_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,3),_AlaTrapInetStationPort_Type())
alaTrapInetStationPort.setMaxAccess(_D)
if mibBuilder.loadTexts:alaTrapInetStationPort.setStatus(_A)
_AlaTrapInetStationRowStatus_Type=RowStatus
_AlaTrapInetStationRowStatus_Object=MibTableColumn
alaTrapInetStationRowStatus=_AlaTrapInetStationRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,4),_AlaTrapInetStationRowStatus_Type())
alaTrapInetStationRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaTrapInetStationRowStatus.setStatus(_A)
class _AlaTrapInetStationProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3)))
_AlaTrapInetStationProtocol_Type.__name__=_C
_AlaTrapInetStationProtocol_Object=MibTableColumn
alaTrapInetStationProtocol=_AlaTrapInetStationProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,5),_AlaTrapInetStationProtocol_Type())
alaTrapInetStationProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:alaTrapInetStationProtocol.setStatus(_A)
class _AlaTrapInetStationUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaTrapInetStationUser_Type.__name__=_G
_AlaTrapInetStationUser_Object=MibTableColumn
alaTrapInetStationUser=_AlaTrapInetStationUser_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,6),_AlaTrapInetStationUser_Type())
alaTrapInetStationUser.setMaxAccess(_D)
if mibBuilder.loadTexts:alaTrapInetStationUser.setStatus(_A)
class _AlaTrapInetStationReplay_Type(Unsigned32):defaultValue=0
_AlaTrapInetStationReplay_Type.__name__=_E
_AlaTrapInetStationReplay_Object=MibTableColumn
alaTrapInetStationReplay=_AlaTrapInetStationReplay_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,7),_AlaTrapInetStationReplay_Type())
alaTrapInetStationReplay.setMaxAccess(_D)
if mibBuilder.loadTexts:alaTrapInetStationReplay.setStatus(_A)
class _AlaTrapInetStationNextSeq_Type(Unsigned32):defaultValue=0
_AlaTrapInetStationNextSeq_Type.__name__=_E
_AlaTrapInetStationNextSeq_Object=MibTableColumn
alaTrapInetStationNextSeq=_AlaTrapInetStationNextSeq_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,6,1,8),_AlaTrapInetStationNextSeq_Type())
alaTrapInetStationNextSeq.setMaxAccess(_F)
if mibBuilder.loadTexts:alaTrapInetStationNextSeq.setStatus(_A)
_AlaTrapInetFilterTable_Object=MibTable
alaTrapInetFilterTable=_AlaTrapInetFilterTable_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,7))
if mibBuilder.loadTexts:alaTrapInetFilterTable.setStatus(_A)
_AlaTrapInetFilterEntry_Object=MibTableRow
alaTrapInetFilterEntry=_AlaTrapInetFilterEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,7,1))
alaTrapInetFilterEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_H))
if mibBuilder.loadTexts:alaTrapInetFilterEntry.setStatus(_A)
class _AlaTrapInetFilterStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_AlaTrapInetFilterStatus_Type.__name__=_C
_AlaTrapInetFilterStatus_Object=MibTableColumn
alaTrapInetFilterStatus=_AlaTrapInetFilterStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,1,7,1,1),_AlaTrapInetFilterStatus_Type())
alaTrapInetFilterStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:alaTrapInetFilterStatus.setStatus(_A)
_TrapNotif_ObjectIdentity=ObjectIdentity
trapNotif=_TrapNotif_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,3))
_TrapAbsorStamp_Type=Unsigned32
_TrapAbsorStamp_Object=MibScalar
trapAbsorStamp=_TrapAbsorStamp_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,3,1),_TrapAbsorStamp_Type())
trapAbsorStamp.setMaxAccess(_K)
if mibBuilder.loadTexts:trapAbsorStamp.setStatus(_A)
class _TrapAbsorTrapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_TrapAbsorTrapId_Type.__name__=_C
_TrapAbsorTrapId_Object=MibScalar
trapAbsorTrapId=_TrapAbsorTrapId_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,3,2),_TrapAbsorTrapId_Type())
trapAbsorTrapId.setMaxAccess(_K)
if mibBuilder.loadTexts:trapAbsorTrapId.setStatus(_A)
_TrapAbsorCounter_Type=Unsigned32
_TrapAbsorCounter_Object=MibScalar
trapAbsorCounter=_TrapAbsorCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,3,3),_TrapAbsorCounter_Type())
trapAbsorCounter.setMaxAccess(_K)
if mibBuilder.loadTexts:trapAbsorCounter.setStatus(_A)
_TrapAbsorTime_Type=Unsigned32
_TrapAbsorTime_Object=MibScalar
trapAbsorTime=_TrapAbsorTime_Object((1,3,6,1,4,1,6486,800,1,2,1,2,1,1,3,4),_TrapAbsorTime_Type())
trapAbsorTime.setMaxAccess(_K)
if mibBuilder.loadTexts:trapAbsorTime.setStatus(_A)
_AlcatelIND1TrapMgrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1TrapMgrMIBConformance=_AlcatelIND1TrapMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,2,1,2))
if mibBuilder.loadTexts:alcatelIND1TrapMgrMIBConformance.setStatus(_A)
_AlcatelIND1TrapMgrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1TrapMgrMIBGroups=_AlcatelIND1TrapMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,2,1,2,1))
if mibBuilder.loadTexts:alcatelIND1TrapMgrMIBGroups.setStatus(_A)
_AlcatelIND1TrapMgrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1TrapMgrMIBCompliances=_AlcatelIND1TrapMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,2,1,2,2))
if mibBuilder.loadTexts:alcatelIND1TrapMgrMIBCompliances.setStatus(_A)
trapMgtGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,2,1,2,1,1))
trapMgtGroup.setObjects(*((_B,_H),(_B,_V),(_B,_W),(_B,_X),(_B,_I),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:trapMgtGroup.setStatus(_A)
trapNotifGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,2,1,2,1,3))
trapNotifGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:trapNotifGroup.setStatus(_A)
trapAbsorptionTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,12,0,1))
trapAbsorptionTrap.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:trapAbsorptionTrap.setStatus(_A)
trapTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,2,1,2,1,2))
trapTrapsGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:trapTrapsGroup.setStatus(_A)
alcatelIND1TrapMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,2,1,2,2,1))
alcatelIND1TrapMgrMIBCompliance.setObjects(*((_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:alcatelIND1TrapMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1TrapMgrMIB':alcatelIND1TrapMgrMIB,'alcatelIND1TrapMgrMIBObjects':alcatelIND1TrapMgrMIBObjects,'trapMgt':trapMgt,'trapConfigTable':trapConfigTable,'trapConfigEntry':trapConfigEntry,_H:trapIndex,_V:trapName,_W:trapFamily,_X:trapAbsorbPeriod,'trapStationTable':trapStationTable,'trapStationEntry':trapStationEntry,_I:trapStationIP,_Y:trapStationPort,_Z:trapStationRowStatus,_a:trapStationProtocol,_b:trapStationUser,_c:trapStationReplay,_d:trapStationNextSeq,'trapFilterTable':trapFilterTable,'trapFilterEntry':trapFilterEntry,_e:trapFilterStatus,_f:trapAbsorption,_g:trapToWebView,'alaTrapInetStationTable':alaTrapInetStationTable,'alaTrapInetStationEntry':alaTrapInetStationEntry,_L:alaTrapInetStationIPType,_M:alaTrapInetStationIP,_h:alaTrapInetStationPort,_i:alaTrapInetStationRowStatus,_j:alaTrapInetStationProtocol,_k:alaTrapInetStationUser,_l:alaTrapInetStationReplay,_m:alaTrapInetStationNextSeq,'alaTrapInetFilterTable':alaTrapInetFilterTable,'alaTrapInetFilterEntry':alaTrapInetFilterEntry,_n:alaTrapInetFilterStatus,'trapNotif':trapNotif,_N:trapAbsorStamp,_O:trapAbsorTrapId,_P:trapAbsorCounter,_Q:trapAbsorTime,'alcatelIND1TrapMgrMIBConformance':alcatelIND1TrapMgrMIBConformance,'alcatelIND1TrapMgrMIBGroups':alcatelIND1TrapMgrMIBGroups,_p:trapMgtGroup,_q:trapTrapsGroup,_r:trapNotifGroup,'alcatelIND1TrapMgrMIBCompliances':alcatelIND1TrapMgrMIBCompliances,'alcatelIND1TrapMgrMIBCompliance':alcatelIND1TrapMgrMIBCompliance,_o:trapAbsorptionTrap})