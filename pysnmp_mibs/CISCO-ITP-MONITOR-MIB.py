_w='ciscoItpmNotificationsGroupRev1'
_v='ciscoItpmConnGroupRev1'
_u='ciscoItpmNotificationsGroup'
_t='ciscoItpmConnGroup'
_s='ciscoItpMonitorState'
_r='cItpmMonitorStateNotifEnabled'
_q='cItpmLinkSentBitsRate'
_p='cItpmLinkSentMsuRate'
_o='cItpmLinkSentMsuDrops'
_n='cItpmLinkSentMsus'
_m='cItpmLinkRcvdBitsRate'
_l='cItpmLinkRcvdMsuRate'
_k='cItpmLinkRcvdMsuDrops'
_j='cItpmLinkRcvdMsus'
_i='cItpmLinkStatus'
_h='cItpmLinkSlotNumber'
_g='cItpmLinkDescription'
_f='bits per second'
_e='MSUs per second'
_d='cItpmLinkNumber'
_c='inactive'
_b='active'
_a='not-accessible'
_Z='Gauge32'
_Y='SnmpAdminString'
_X='ciscoItpmLinkGroup'
_W='ciscoItpMonitorCongestion'
_V='deprecated'
_U='cItpmConnCongCounts'
_T='cItpmConnQueueDepth'
_S='cItpmConnFastStart'
_R='cItpmConnRcvWindowSize'
_Q='cItpmConnCongAbate'
_P='cItpmConnCongOnset'
_O='cItpmConnMaxQDepth'
_N='cItpmConnKeepAlive'
_M='cItpmCongestionNotifEnabled'
_L='cItpmConnPortNumber'
_K='Integer32'
_J='cItpmConnCongestion'
_I='cItpmConnMonitorState'
_H='MSUs'
_G='packets'
_F='TruthValue'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-ITP-MONITOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_Z,_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
ciscoItpmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,379))
if mibBuilder.loadTexts:ciscoItpmMIB.setRevisions(('2004-07-20 00:00','2003-10-31 00:00'))
_CiscoItpmMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoItpmMIBNotifs=_CiscoItpmMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,379,0))
_CiscoItpmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoItpmMIBObjects=_CiscoItpmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,379,1))
_CItpmConn_ObjectIdentity=ObjectIdentity
cItpmConn=_CItpmConn_ObjectIdentity((1,3,6,1,4,1,9,9,379,1,1))
_CItpmConnTable_Object=MibTable
cItpmConnTable=_CItpmConnTable_Object((1,3,6,1,4,1,9,9,379,1,1,1))
if mibBuilder.loadTexts:cItpmConnTable.setStatus(_B)
_CItpmConnTableEntry_Object=MibTableRow
cItpmConnTableEntry=_CItpmConnTableEntry_Object((1,3,6,1,4,1,9,9,379,1,1,1,1))
cItpmConnTableEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:cItpmConnTableEntry.setStatus(_B)
_CItpmConnPortNumber_Type=InetPortNumber
_CItpmConnPortNumber_Object=MibTableColumn
cItpmConnPortNumber=_CItpmConnPortNumber_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,1),_CItpmConnPortNumber_Type())
cItpmConnPortNumber.setMaxAccess(_a)
if mibBuilder.loadTexts:cItpmConnPortNumber.setStatus(_B)
class _CItpmConnKeepAlive_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_CItpmConnKeepAlive_Type.__name__=_D
_CItpmConnKeepAlive_Object=MibTableColumn
cItpmConnKeepAlive=_CItpmConnKeepAlive_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,2),_CItpmConnKeepAlive_Type())
cItpmConnKeepAlive.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmConnKeepAlive.setStatus(_B)
if mibBuilder.loadTexts:cItpmConnKeepAlive.setUnits('milliseconds')
class _CItpmConnMaxQDepth_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_CItpmConnMaxQDepth_Type.__name__=_D
_CItpmConnMaxQDepth_Object=MibTableColumn
cItpmConnMaxQDepth=_CItpmConnMaxQDepth_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,3),_CItpmConnMaxQDepth_Type())
cItpmConnMaxQDepth.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmConnMaxQDepth.setStatus(_B)
if mibBuilder.loadTexts:cItpmConnMaxQDepth.setUnits(_G)
class _CItpmConnCongOnset_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100000))
_CItpmConnCongOnset_Type.__name__=_D
_CItpmConnCongOnset_Object=MibTableColumn
cItpmConnCongOnset=_CItpmConnCongOnset_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,4),_CItpmConnCongOnset_Type())
cItpmConnCongOnset.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmConnCongOnset.setStatus(_B)
if mibBuilder.loadTexts:cItpmConnCongOnset.setUnits(_G)
class _CItpmConnCongAbate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CItpmConnCongAbate_Type.__name__=_D
_CItpmConnCongAbate_Object=MibTableColumn
cItpmConnCongAbate=_CItpmConnCongAbate_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,5),_CItpmConnCongAbate_Type())
cItpmConnCongAbate.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmConnCongAbate.setStatus(_B)
if mibBuilder.loadTexts:cItpmConnCongAbate.setUnits(_G)
class _CItpmConnRcvWindowSize_Type(Unsigned32):defaultValue=200000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_CItpmConnRcvWindowSize_Type.__name__=_D
_CItpmConnRcvWindowSize_Object=MibTableColumn
cItpmConnRcvWindowSize=_CItpmConnRcvWindowSize_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,6),_CItpmConnRcvWindowSize_Type())
cItpmConnRcvWindowSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmConnRcvWindowSize.setStatus(_B)
if mibBuilder.loadTexts:cItpmConnRcvWindowSize.setUnits('bytes')
class _CItpmConnFastStart_Type(TruthValue):defaultValue=2
_CItpmConnFastStart_Type.__name__=_F
_CItpmConnFastStart_Object=MibTableColumn
cItpmConnFastStart=_CItpmConnFastStart_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,7),_CItpmConnFastStart_Type())
cItpmConnFastStart.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmConnFastStart.setStatus(_B)
class _CItpmConnQueueDepth_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CItpmConnQueueDepth_Type.__name__=_Z
_CItpmConnQueueDepth_Object=MibTableColumn
cItpmConnQueueDepth=_CItpmConnQueueDepth_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,8),_CItpmConnQueueDepth_Type())
cItpmConnQueueDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmConnQueueDepth.setStatus(_B)
if mibBuilder.loadTexts:cItpmConnQueueDepth.setUnits(_G)
class _CItpmConnMonitorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_CItpmConnMonitorState_Type.__name__=_K
_CItpmConnMonitorState_Object=MibTableColumn
cItpmConnMonitorState=_CItpmConnMonitorState_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,9),_CItpmConnMonitorState_Type())
cItpmConnMonitorState.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmConnMonitorState.setStatus(_B)
_CItpmConnCongestion_Type=TruthValue
_CItpmConnCongestion_Object=MibTableColumn
cItpmConnCongestion=_CItpmConnCongestion_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,10),_CItpmConnCongestion_Type())
cItpmConnCongestion.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmConnCongestion.setStatus(_B)
_CItpmConnCongCounts_Type=Counter32
_CItpmConnCongCounts_Object=MibTableColumn
cItpmConnCongCounts=_CItpmConnCongCounts_Object((1,3,6,1,4,1,9,9,379,1,1,1,1,11),_CItpmConnCongCounts_Type())
cItpmConnCongCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmConnCongCounts.setStatus(_B)
if mibBuilder.loadTexts:cItpmConnCongCounts.setUnits('occurences')
_CItpmLinkTable_Object=MibTable
cItpmLinkTable=_CItpmLinkTable_Object((1,3,6,1,4,1,9,9,379,1,1,2))
if mibBuilder.loadTexts:cItpmLinkTable.setStatus(_B)
_CItpmLinkTableEntry_Object=MibTableRow
cItpmLinkTableEntry=_CItpmLinkTableEntry_Object((1,3,6,1,4,1,9,9,379,1,1,2,1))
cItpmLinkTableEntry.setIndexNames((0,_A,_L),(0,_A,_d))
if mibBuilder.loadTexts:cItpmLinkTableEntry.setStatus(_B)
class _CItpmLinkNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CItpmLinkNumber_Type.__name__=_D
_CItpmLinkNumber_Object=MibTableColumn
cItpmLinkNumber=_CItpmLinkNumber_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,1),_CItpmLinkNumber_Type())
cItpmLinkNumber.setMaxAccess(_a)
if mibBuilder.loadTexts:cItpmLinkNumber.setStatus(_B)
class _CItpmLinkDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CItpmLinkDescription_Type.__name__=_Y
_CItpmLinkDescription_Object=MibTableColumn
cItpmLinkDescription=_CItpmLinkDescription_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,2),_CItpmLinkDescription_Type())
cItpmLinkDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkDescription.setStatus(_B)
class _CItpmLinkSlotNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CItpmLinkSlotNumber_Type.__name__=_D
_CItpmLinkSlotNumber_Object=MibTableColumn
cItpmLinkSlotNumber=_CItpmLinkSlotNumber_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,3),_CItpmLinkSlotNumber_Type())
cItpmLinkSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkSlotNumber.setStatus(_B)
class _CItpmLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_CItpmLinkStatus_Type.__name__=_K
_CItpmLinkStatus_Object=MibTableColumn
cItpmLinkStatus=_CItpmLinkStatus_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,4),_CItpmLinkStatus_Type())
cItpmLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkStatus.setStatus(_B)
_CItpmLinkRcvdMsus_Type=Counter32
_CItpmLinkRcvdMsus_Object=MibTableColumn
cItpmLinkRcvdMsus=_CItpmLinkRcvdMsus_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,5),_CItpmLinkRcvdMsus_Type())
cItpmLinkRcvdMsus.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkRcvdMsus.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkRcvdMsus.setUnits(_H)
_CItpmLinkRcvdMsuDrops_Type=Counter32
_CItpmLinkRcvdMsuDrops_Object=MibTableColumn
cItpmLinkRcvdMsuDrops=_CItpmLinkRcvdMsuDrops_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,6),_CItpmLinkRcvdMsuDrops_Type())
cItpmLinkRcvdMsuDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkRcvdMsuDrops.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkRcvdMsuDrops.setUnits(_H)
_CItpmLinkRcvdMsuRate_Type=Gauge32
_CItpmLinkRcvdMsuRate_Object=MibTableColumn
cItpmLinkRcvdMsuRate=_CItpmLinkRcvdMsuRate_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,7),_CItpmLinkRcvdMsuRate_Type())
cItpmLinkRcvdMsuRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkRcvdMsuRate.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkRcvdMsuRate.setUnits(_e)
_CItpmLinkRcvdBitsRate_Type=Gauge32
_CItpmLinkRcvdBitsRate_Object=MibTableColumn
cItpmLinkRcvdBitsRate=_CItpmLinkRcvdBitsRate_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,8),_CItpmLinkRcvdBitsRate_Type())
cItpmLinkRcvdBitsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkRcvdBitsRate.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkRcvdBitsRate.setUnits(_f)
_CItpmLinkSentMsus_Type=Counter32
_CItpmLinkSentMsus_Object=MibTableColumn
cItpmLinkSentMsus=_CItpmLinkSentMsus_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,9),_CItpmLinkSentMsus_Type())
cItpmLinkSentMsus.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkSentMsus.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkSentMsus.setUnits(_H)
_CItpmLinkSentMsuDrops_Type=Counter32
_CItpmLinkSentMsuDrops_Object=MibTableColumn
cItpmLinkSentMsuDrops=_CItpmLinkSentMsuDrops_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,10),_CItpmLinkSentMsuDrops_Type())
cItpmLinkSentMsuDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkSentMsuDrops.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkSentMsuDrops.setUnits(_H)
_CItpmLinkSentMsuRate_Type=Gauge32
_CItpmLinkSentMsuRate_Object=MibTableColumn
cItpmLinkSentMsuRate=_CItpmLinkSentMsuRate_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,11),_CItpmLinkSentMsuRate_Type())
cItpmLinkSentMsuRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkSentMsuRate.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkSentMsuRate.setUnits(_e)
_CItpmLinkSentBitsRate_Type=Gauge32
_CItpmLinkSentBitsRate_Object=MibTableColumn
cItpmLinkSentBitsRate=_CItpmLinkSentBitsRate_Object((1,3,6,1,4,1,9,9,379,1,1,2,1,12),_CItpmLinkSentBitsRate_Type())
cItpmLinkSentBitsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpmLinkSentBitsRate.setStatus(_B)
if mibBuilder.loadTexts:cItpmLinkSentBitsRate.setUnits(_f)
_CItpmLink_ObjectIdentity=ObjectIdentity
cItpmLink=_CItpmLink_ObjectIdentity((1,3,6,1,4,1,9,9,379,1,2))
class _CItpmCongestionNotifEnabled_Type(TruthValue):defaultValue=2
_CItpmCongestionNotifEnabled_Type.__name__=_F
_CItpmCongestionNotifEnabled_Object=MibScalar
cItpmCongestionNotifEnabled=_CItpmCongestionNotifEnabled_Object((1,3,6,1,4,1,9,9,379,1,3),_CItpmCongestionNotifEnabled_Type())
cItpmCongestionNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmCongestionNotifEnabled.setStatus(_B)
class _CItpmMonitorStateNotifEnabled_Type(TruthValue):defaultValue=2
_CItpmMonitorStateNotifEnabled_Type.__name__=_F
_CItpmMonitorStateNotifEnabled_Object=MibScalar
cItpmMonitorStateNotifEnabled=_CItpmMonitorStateNotifEnabled_Object((1,3,6,1,4,1,9,9,379,1,4),_CItpmMonitorStateNotifEnabled_Type())
cItpmMonitorStateNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cItpmMonitorStateNotifEnabled.setStatus(_B)
_CiscoItpmMIBConform_ObjectIdentity=ObjectIdentity
ciscoItpmMIBConform=_CiscoItpmMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,379,2))
_CiscoItpmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoItpmMIBCompliances=_CiscoItpmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,379,2,1))
_CiscoItpmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoItpmMIBGroups=_CiscoItpmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,379,2,2))
ciscoItpmConnGroup=ObjectGroup((1,3,6,1,4,1,9,9,379,2,2,1))
ciscoItpmConnGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_I),(_A,_J),(_A,_U)))
if mibBuilder.loadTexts:ciscoItpmConnGroup.setStatus(_V)
ciscoItpmLinkGroup=ObjectGroup((1,3,6,1,4,1,9,9,379,2,2,2))
ciscoItpmLinkGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoItpmLinkGroup.setStatus(_B)
ciscoItpmConnGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,379,2,2,4))
ciscoItpmConnGroupRev1.setObjects(*((_A,_M),(_A,_r),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_I),(_A,_J),(_A,_U)))
if mibBuilder.loadTexts:ciscoItpmConnGroupRev1.setStatus(_B)
ciscoItpMonitorCongestion=NotificationType((1,3,6,1,4,1,9,9,379,0,1))
ciscoItpMonitorCongestion.setObjects((_A,_J))
if mibBuilder.loadTexts:ciscoItpMonitorCongestion.setStatus(_B)
ciscoItpMonitorState=NotificationType((1,3,6,1,4,1,9,9,379,0,2))
ciscoItpMonitorState.setObjects((_A,_I))
if mibBuilder.loadTexts:ciscoItpMonitorState.setStatus(_B)
ciscoItpmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,379,2,2,3))
ciscoItpmNotificationsGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:ciscoItpmNotificationsGroup.setStatus(_V)
ciscoItpmNotificationsGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,379,2,2,5))
ciscoItpmNotificationsGroupRev1.setObjects(*((_A,_W),(_A,_s)))
if mibBuilder.loadTexts:ciscoItpmNotificationsGroupRev1.setStatus(_B)
ciscoItpmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,379,2,1,1))
ciscoItpmMIBCompliance.setObjects(*((_A,_t),(_A,_X),(_A,_u)))
if mibBuilder.loadTexts:ciscoItpmMIBCompliance.setStatus(_V)
ciscoItpmMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,379,2,1,2))
ciscoItpmMIBComplianceRev1.setObjects(*((_A,_v),(_A,_X),(_A,_w)))
if mibBuilder.loadTexts:ciscoItpmMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoItpmMIB':ciscoItpmMIB,'ciscoItpmMIBNotifs':ciscoItpmMIBNotifs,_W:ciscoItpMonitorCongestion,_s:ciscoItpMonitorState,'ciscoItpmMIBObjects':ciscoItpmMIBObjects,'cItpmConn':cItpmConn,'cItpmConnTable':cItpmConnTable,'cItpmConnTableEntry':cItpmConnTableEntry,_L:cItpmConnPortNumber,_N:cItpmConnKeepAlive,_O:cItpmConnMaxQDepth,_P:cItpmConnCongOnset,_Q:cItpmConnCongAbate,_R:cItpmConnRcvWindowSize,_S:cItpmConnFastStart,_T:cItpmConnQueueDepth,_I:cItpmConnMonitorState,_J:cItpmConnCongestion,_U:cItpmConnCongCounts,'cItpmLinkTable':cItpmLinkTable,'cItpmLinkTableEntry':cItpmLinkTableEntry,_d:cItpmLinkNumber,_g:cItpmLinkDescription,_h:cItpmLinkSlotNumber,_i:cItpmLinkStatus,_j:cItpmLinkRcvdMsus,_k:cItpmLinkRcvdMsuDrops,_l:cItpmLinkRcvdMsuRate,_m:cItpmLinkRcvdBitsRate,_n:cItpmLinkSentMsus,_o:cItpmLinkSentMsuDrops,_p:cItpmLinkSentMsuRate,_q:cItpmLinkSentBitsRate,'cItpmLink':cItpmLink,_M:cItpmCongestionNotifEnabled,_r:cItpmMonitorStateNotifEnabled,'ciscoItpmMIBConform':ciscoItpmMIBConform,'ciscoItpmMIBCompliances':ciscoItpmMIBCompliances,'ciscoItpmMIBCompliance':ciscoItpmMIBCompliance,'ciscoItpmMIBComplianceRev1':ciscoItpmMIBComplianceRev1,'ciscoItpmMIBGroups':ciscoItpmMIBGroups,_t:ciscoItpmConnGroup,_X:ciscoItpmLinkGroup,_u:ciscoItpmNotificationsGroup,_v:ciscoItpmConnGroupRev1,_w:ciscoItpmNotificationsGroupRev1})