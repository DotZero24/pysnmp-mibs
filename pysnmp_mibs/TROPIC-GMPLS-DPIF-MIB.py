_AD='tnGmplsDBLinkGroup'
_AC='tnGmplsTELinkGroup'
_AB='tnGmplsDpifObjsGroup'
_AA='tnGmplsTELinkRowStatus'
_A9='tnGmplsTELinkAlarmState'
_A8='tnGmplsTELinkMaintState'
_A7='tnGmplsTELinkOperationalState'
_A6='tnGmplsTELinkAdminStatus'
_A5='tnGmplsTELinkLatency'
_A4='tnGmplsTELinkSRLG'
_A3='tnGmplsTELinkColor'
_A2='tnGmplsTELinkMetric'
_A1='tnGmplsTELinkName'
_A0='tnGmplsTELinkTNA'
_z='tnGmplsTELinkRemoteCPNodeId'
_y='tnGmplsTELinkRemoteSubnodeId'
_x='tnGmplsTELinkRemoteIfId'
_w='tnGmplsDBLinkRowStatus'
_v='tnGmplsDBLink3RIndex'
_u='tnGmplsDBLinkAlarmState'
_t='tnGmplsDBLinkMaintState'
_s='tnGmplsDBLinkOperationalState'
_r='tnGmplsDBLinkAdminStatus'
_q='tnGmplsDBLinkWTR'
_p='tnGmplsDBLinkUseInFiber'
_o='tnGmplsDBLinkACD'
_n='tnGmplsDBLinkTEId'
_m='tnGmplsDBLinkType'
_l='tnGmplsDBLinkName'
_k='tnGmplsDBLinkRemoteIfId'
_j='tnGmplsDpifAttributeTotal'
_i='tnGmplsTELinkIfId'
_h='noAlarm'
_g='hardwareUnavailableOTU'
_f='localOTUAlarm'
_e='hardwareDegraded'
_d='dbAlarm'
_c='remoteSDAlarm'
_b='localSDAlarm'
_a='remoteWTR'
_Z='localWTR'
_Y='otherMgrConnection'
_X='hardwareClash'
_W='remoteDBDown'
_V='linkSummaryMismatch'
_U='cpDown'
_T='allDBDown'
_S='dbDown'
_R='disabled'
_Q='neUnavailable'
_P='hardwareUnavailable'
_O='itcAlarm'
_N='remoteAlarm'
_M='localAlarm'
_L='linkMaintenance'
_K='shuttingdown'
_J='not-accessible'
_I='tnGmplsDBLinkIfId'
_H='Unsigned32'
_G='up'
_F='down'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='TROPIC-GMPLS-DPIF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
tnGmplsMIBModules,tnGmplsObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnGmplsMIBModules','tnGmplsObjs')
tnGmplsDpifMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,6,2))
if mibBuilder.loadTexts:tnGmplsDpifMibModule.setRevisions(('2018-02-23 12:00','2017-07-07 12:00','2016-11-16 12:00','2013-06-27 12:00'))
_TnGmplsDpifMIB_ObjectIdentity=ObjectIdentity
tnGmplsDpifMIB=_TnGmplsDpifMIB_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,2))
_TnGmplsDpifObjs_ObjectIdentity=ObjectIdentity
tnGmplsDpifObjs=_TnGmplsDpifObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,2,1))
_TnGmplsDpifAttributeTotal_Type=Integer32
_TnGmplsDpifAttributeTotal_Object=MibScalar
tnGmplsDpifAttributeTotal=_TnGmplsDpifAttributeTotal_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,1),_TnGmplsDpifAttributeTotal_Type())
tnGmplsDpifAttributeTotal.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsDpifAttributeTotal.setStatus(_A)
_TnGmplsDBLinkTable_Object=MibTable
tnGmplsDBLinkTable=_TnGmplsDBLinkTable_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2))
if mibBuilder.loadTexts:tnGmplsDBLinkTable.setStatus(_A)
_TnGmplsDBLinkEntry_Object=MibTableRow
tnGmplsDBLinkEntry=_TnGmplsDBLinkEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1))
tnGmplsDBLinkEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:tnGmplsDBLinkEntry.setStatus(_A)
_TnGmplsDBLinkIfId_Type=Unsigned32
_TnGmplsDBLinkIfId_Object=MibTableColumn
tnGmplsDBLinkIfId=_TnGmplsDBLinkIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,1),_TnGmplsDBLinkIfId_Type())
tnGmplsDBLinkIfId.setMaxAccess(_J)
if mibBuilder.loadTexts:tnGmplsDBLinkIfId.setStatus(_A)
_TnGmplsDBLinkRemoteIfId_Type=Unsigned32
_TnGmplsDBLinkRemoteIfId_Object=MibTableColumn
tnGmplsDBLinkRemoteIfId=_TnGmplsDBLinkRemoteIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,2),_TnGmplsDBLinkRemoteIfId_Type())
tnGmplsDBLinkRemoteIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkRemoteIfId.setStatus(_A)
_TnGmplsDBLinkName_Type=DisplayString
_TnGmplsDBLinkName_Object=MibTableColumn
tnGmplsDBLinkName=_TnGmplsDBLinkName_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,3),_TnGmplsDBLinkName_Type())
tnGmplsDBLinkName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkName.setStatus(_A)
class _TnGmplsDBLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('drop',1),('nni',2),('enni',3),('ennig',4),('uni',5),('unistar',6),('regen3R',7)))
_TnGmplsDBLinkType_Type.__name__=_D
_TnGmplsDBLinkType_Object=MibTableColumn
tnGmplsDBLinkType=_TnGmplsDBLinkType_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,4),_TnGmplsDBLinkType_Type())
tnGmplsDBLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkType.setStatus(_A)
_TnGmplsDBLinkTEId_Type=Unsigned32
_TnGmplsDBLinkTEId_Object=MibTableColumn
tnGmplsDBLinkTEId=_TnGmplsDBLinkTEId_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,5),_TnGmplsDBLinkTEId_Type())
tnGmplsDBLinkTEId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkTEId.setStatus(_A)
class _TnGmplsDBLinkACD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('empty',1),('cp',2),('cpmp',3),('mp',4)))
_TnGmplsDBLinkACD_Type.__name__=_D
_TnGmplsDBLinkACD_Object=MibTableColumn
tnGmplsDBLinkACD=_TnGmplsDBLinkACD_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,6),_TnGmplsDBLinkACD_Type())
tnGmplsDBLinkACD.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkACD.setStatus(_A)
_TnGmplsDBLinkUseInFiber_Type=TruthValue
_TnGmplsDBLinkUseInFiber_Object=MibTableColumn
tnGmplsDBLinkUseInFiber=_TnGmplsDBLinkUseInFiber_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,7),_TnGmplsDBLinkUseInFiber_Type())
tnGmplsDBLinkUseInFiber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkUseInFiber.setStatus(_A)
_TnGmplsDBLinkWTR_Type=Unsigned32
_TnGmplsDBLinkWTR_Object=MibTableColumn
tnGmplsDBLinkWTR=_TnGmplsDBLinkWTR_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,8),_TnGmplsDBLinkWTR_Type())
tnGmplsDBLinkWTR.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkWTR.setStatus(_A)
class _TnGmplsDBLinkAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_K,3)))
_TnGmplsDBLinkAdminStatus_Type.__name__=_D
_TnGmplsDBLinkAdminStatus_Object=MibTableColumn
tnGmplsDBLinkAdminStatus=_TnGmplsDBLinkAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,9),_TnGmplsDBLinkAdminStatus_Type())
tnGmplsDBLinkAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkAdminStatus.setStatus(_A)
class _TnGmplsDBLinkOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TnGmplsDBLinkOperationalState_Type.__name__=_D
_TnGmplsDBLinkOperationalState_Object=MibTableColumn
tnGmplsDBLinkOperationalState=_TnGmplsDBLinkOperationalState_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,10),_TnGmplsDBLinkOperationalState_Type())
tnGmplsDBLinkOperationalState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsDBLinkOperationalState.setStatus(_A)
class _TnGmplsDBLinkMaintState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,6)))
_TnGmplsDBLinkMaintState_Type.__name__=_D
_TnGmplsDBLinkMaintState_Object=MibTableColumn
tnGmplsDBLinkMaintState=_TnGmplsDBLinkMaintState_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,11),_TnGmplsDBLinkMaintState_Type())
tnGmplsDBLinkMaintState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkMaintState.setStatus(_A)
class _TnGmplsDBLinkAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8),(_U,9),(_V,10),(_W,11),(_X,12),(_Y,13),(_Z,14),(_a,15),(_b,16),(_c,17),(_d,18),(_e,19),(_f,20),(_g,21),('ltcer',22),('ue',23),('tca',24),(_h,25)))
_TnGmplsDBLinkAlarmState_Type.__name__=_D
_TnGmplsDBLinkAlarmState_Object=MibTableColumn
tnGmplsDBLinkAlarmState=_TnGmplsDBLinkAlarmState_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,12),_TnGmplsDBLinkAlarmState_Type())
tnGmplsDBLinkAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsDBLinkAlarmState.setStatus(_A)
_TnGmplsDBLink3RIndex_Type=Unsigned32
_TnGmplsDBLink3RIndex_Object=MibTableColumn
tnGmplsDBLink3RIndex=_TnGmplsDBLink3RIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,13),_TnGmplsDBLink3RIndex_Type())
tnGmplsDBLink3RIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsDBLink3RIndex.setStatus(_A)
_TnGmplsDBLinkRowStatus_Type=RowStatus
_TnGmplsDBLinkRowStatus_Object=MibTableColumn
tnGmplsDBLinkRowStatus=_TnGmplsDBLinkRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,2,1,14),_TnGmplsDBLinkRowStatus_Type())
tnGmplsDBLinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDBLinkRowStatus.setStatus(_A)
_TnGmplsTELinkTable_Object=MibTable
tnGmplsTELinkTable=_TnGmplsTELinkTable_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3))
if mibBuilder.loadTexts:tnGmplsTELinkTable.setStatus(_A)
_TnGmplsTELinkEntry_Object=MibTableRow
tnGmplsTELinkEntry=_TnGmplsTELinkEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1))
tnGmplsTELinkEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:tnGmplsTELinkEntry.setStatus(_A)
class _TnGmplsTELinkIfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100000,999999))
_TnGmplsTELinkIfId_Type.__name__=_H
_TnGmplsTELinkIfId_Object=MibTableColumn
tnGmplsTELinkIfId=_TnGmplsTELinkIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,1),_TnGmplsTELinkIfId_Type())
tnGmplsTELinkIfId.setMaxAccess(_J)
if mibBuilder.loadTexts:tnGmplsTELinkIfId.setStatus(_A)
_TnGmplsTELinkRemoteIfId_Type=Unsigned32
_TnGmplsTELinkRemoteIfId_Object=MibTableColumn
tnGmplsTELinkRemoteIfId=_TnGmplsTELinkRemoteIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,2),_TnGmplsTELinkRemoteIfId_Type())
tnGmplsTELinkRemoteIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkRemoteIfId.setStatus(_A)
_TnGmplsTELinkRemoteSubnodeId_Type=Unsigned32
_TnGmplsTELinkRemoteSubnodeId_Object=MibTableColumn
tnGmplsTELinkRemoteSubnodeId=_TnGmplsTELinkRemoteSubnodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,3),_TnGmplsTELinkRemoteSubnodeId_Type())
tnGmplsTELinkRemoteSubnodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkRemoteSubnodeId.setStatus(_A)
_TnGmplsTELinkRemoteCPNodeId_Type=InetAddressIPv4
_TnGmplsTELinkRemoteCPNodeId_Object=MibTableColumn
tnGmplsTELinkRemoteCPNodeId=_TnGmplsTELinkRemoteCPNodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,4),_TnGmplsTELinkRemoteCPNodeId_Type())
tnGmplsTELinkRemoteCPNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkRemoteCPNodeId.setStatus(_A)
_TnGmplsTELinkTNA_Type=InetAddressIPv4
_TnGmplsTELinkTNA_Object=MibTableColumn
tnGmplsTELinkTNA=_TnGmplsTELinkTNA_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,5),_TnGmplsTELinkTNA_Type())
tnGmplsTELinkTNA.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkTNA.setStatus(_A)
_TnGmplsTELinkName_Type=DisplayString
_TnGmplsTELinkName_Object=MibTableColumn
tnGmplsTELinkName=_TnGmplsTELinkName_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,6),_TnGmplsTELinkName_Type())
tnGmplsTELinkName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkName.setStatus(_A)
class _TnGmplsTELinkMetric_Type(Unsigned32):defaultValue=20
_TnGmplsTELinkMetric_Type.__name__=_H
_TnGmplsTELinkMetric_Object=MibTableColumn
tnGmplsTELinkMetric=_TnGmplsTELinkMetric_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,7),_TnGmplsTELinkMetric_Type())
tnGmplsTELinkMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkMetric.setStatus(_A)
class _TnGmplsTELinkColor_Type(Unsigned32):defaultValue=0
_TnGmplsTELinkColor_Type.__name__=_H
_TnGmplsTELinkColor_Object=MibTableColumn
tnGmplsTELinkColor=_TnGmplsTELinkColor_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,8),_TnGmplsTELinkColor_Type())
tnGmplsTELinkColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkColor.setStatus(_A)
_TnGmplsTELinkSRLG_Type=DisplayString
_TnGmplsTELinkSRLG_Object=MibTableColumn
tnGmplsTELinkSRLG=_TnGmplsTELinkSRLG_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,9),_TnGmplsTELinkSRLG_Type())
tnGmplsTELinkSRLG.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkSRLG.setStatus(_A)
class _TnGmplsTELinkLatency_Type(Unsigned32):defaultValue=0
_TnGmplsTELinkLatency_Type.__name__=_H
_TnGmplsTELinkLatency_Object=MibTableColumn
tnGmplsTELinkLatency=_TnGmplsTELinkLatency_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,10),_TnGmplsTELinkLatency_Type())
tnGmplsTELinkLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkLatency.setStatus(_A)
class _TnGmplsTELinkAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_K,3)))
_TnGmplsTELinkAdminStatus_Type.__name__=_D
_TnGmplsTELinkAdminStatus_Object=MibTableColumn
tnGmplsTELinkAdminStatus=_TnGmplsTELinkAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,11),_TnGmplsTELinkAdminStatus_Type())
tnGmplsTELinkAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkAdminStatus.setStatus(_A)
class _TnGmplsTELinkOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TnGmplsTELinkOperationalState_Type.__name__=_D
_TnGmplsTELinkOperationalState_Object=MibTableColumn
tnGmplsTELinkOperationalState=_TnGmplsTELinkOperationalState_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,12),_TnGmplsTELinkOperationalState_Type())
tnGmplsTELinkOperationalState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsTELinkOperationalState.setStatus(_A)
class _TnGmplsTELinkMaintState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,6)))
_TnGmplsTELinkMaintState_Type.__name__=_D
_TnGmplsTELinkMaintState_Object=MibTableColumn
tnGmplsTELinkMaintState=_TnGmplsTELinkMaintState_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,13),_TnGmplsTELinkMaintState_Type())
tnGmplsTELinkMaintState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkMaintState.setStatus(_A)
class _TnGmplsTELinkAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8),(_U,9),(_V,10),(_W,11),(_X,12),(_Y,13),(_Z,14),(_a,15),(_b,16),(_c,17),(_d,18),(_e,19),(_f,20),(_g,21),('ltcer',22),('ue',23),('tca',24),(_h,25)))
_TnGmplsTELinkAlarmState_Type.__name__=_D
_TnGmplsTELinkAlarmState_Object=MibTableColumn
tnGmplsTELinkAlarmState=_TnGmplsTELinkAlarmState_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,14),_TnGmplsTELinkAlarmState_Type())
tnGmplsTELinkAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsTELinkAlarmState.setStatus(_A)
_TnGmplsTELinkRowStatus_Type=RowStatus
_TnGmplsTELinkRowStatus_Object=MibTableColumn
tnGmplsTELinkRowStatus=_TnGmplsTELinkRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,2,1,3,1,15),_TnGmplsTELinkRowStatus_Type())
tnGmplsTELinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsTELinkRowStatus.setStatus(_A)
_TnGmplsDpifConf_ObjectIdentity=ObjectIdentity
tnGmplsDpifConf=_TnGmplsDpifConf_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,2,3))
_TnGmplsDpifGroups_ObjectIdentity=ObjectIdentity
tnGmplsDpifGroups=_TnGmplsDpifGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,2,3,1))
_TnGmplsDpifCompliances_ObjectIdentity=ObjectIdentity
tnGmplsDpifCompliances=_TnGmplsDpifCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,2,3,2))
tnGmplsDpifObjsGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,2,3,1,1))
tnGmplsDpifObjsGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:tnGmplsDpifObjsGroup.setStatus(_A)
tnGmplsDBLinkGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,2,3,1,2))
tnGmplsDBLinkGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:tnGmplsDBLinkGroup.setStatus(_A)
tnGmplsTELinkGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,2,3,1,3))
tnGmplsTELinkGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:tnGmplsTELinkGroup.setStatus(_A)
tnGmplsDpifCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,1,10,1,2,3,2,1))
tnGmplsDpifCompliance.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:tnGmplsDpifCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnGmplsDpifMibModule':tnGmplsDpifMibModule,'tnGmplsDpifMIB':tnGmplsDpifMIB,'tnGmplsDpifObjs':tnGmplsDpifObjs,_j:tnGmplsDpifAttributeTotal,'tnGmplsDBLinkTable':tnGmplsDBLinkTable,'tnGmplsDBLinkEntry':tnGmplsDBLinkEntry,_I:tnGmplsDBLinkIfId,_k:tnGmplsDBLinkRemoteIfId,_l:tnGmplsDBLinkName,_m:tnGmplsDBLinkType,_n:tnGmplsDBLinkTEId,_o:tnGmplsDBLinkACD,_p:tnGmplsDBLinkUseInFiber,_q:tnGmplsDBLinkWTR,_r:tnGmplsDBLinkAdminStatus,_s:tnGmplsDBLinkOperationalState,_t:tnGmplsDBLinkMaintState,_u:tnGmplsDBLinkAlarmState,_v:tnGmplsDBLink3RIndex,_w:tnGmplsDBLinkRowStatus,'tnGmplsTELinkTable':tnGmplsTELinkTable,'tnGmplsTELinkEntry':tnGmplsTELinkEntry,_i:tnGmplsTELinkIfId,_x:tnGmplsTELinkRemoteIfId,_y:tnGmplsTELinkRemoteSubnodeId,_z:tnGmplsTELinkRemoteCPNodeId,_A0:tnGmplsTELinkTNA,_A1:tnGmplsTELinkName,_A2:tnGmplsTELinkMetric,_A3:tnGmplsTELinkColor,_A4:tnGmplsTELinkSRLG,_A5:tnGmplsTELinkLatency,_A6:tnGmplsTELinkAdminStatus,_A7:tnGmplsTELinkOperationalState,_A8:tnGmplsTELinkMaintState,_A9:tnGmplsTELinkAlarmState,_AA:tnGmplsTELinkRowStatus,'tnGmplsDpifConf':tnGmplsDpifConf,'tnGmplsDpifGroups':tnGmplsDpifGroups,_AB:tnGmplsDpifObjsGroup,_AD:tnGmplsDBLinkGroup,_AC:tnGmplsTELinkGroup,'tnGmplsDpifCompliances':tnGmplsDpifCompliances,'tnGmplsDpifCompliance':tnGmplsDpifCompliance})