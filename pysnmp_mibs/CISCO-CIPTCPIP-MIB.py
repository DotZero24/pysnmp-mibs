_AO='ciscoCipTcpIpGroup'
_AN='cipUdpOutDatagrams'
_AM='cipUdpInErrors'
_AL='cipUdpNoPorts'
_AK='cipUdpInDatagrams'
_AJ='cipIcmpOutAddrMaskReps'
_AI='cipIcmpOutAddrMasks'
_AH='cipIcmpOutTimestampReps'
_AG='cipIcmpOutTimestamps'
_AF='cipIcmpOutEchoReps'
_AE='cipIcmpOutEchos'
_AD='cipIcmpOutDestUnreachs'
_AC='cipIcmpOutErrors'
_AB='cipIcmpOutMsgs'
_AA='cipIcmpInAddrMaskReps'
_A9='cipIcmpInEchos'
_A8='cipIcmpInRedirects'
_A7='cipIcmpInSrcQuenchs'
_A6='cipIcmpInParmProbs'
_A5='cipIcmpInTimeExcds'
_A4='cipIcmpInDestUnreachs'
_A3='cipIcmpInErrors'
_A2='cipIcmpInMsgs'
_A1='cipTcpConnOutHCBytes'
_A0='cipTcpConnOutBytes'
_z='cipTcpConnInHCBytes'
_y='cipTcpConnInBytes'
_x='cipTcpConnState'
_w='cipTcpOutRsts'
_v='cipTcpInErrs'
_u='cipTcpRetransSegs'
_t='cipTcpOutSegs'
_s='cipTcpInSegs'
_r='cipTcpCurrEstab'
_q='cipTcpEstabResets'
_p='cipTcpAttemptFails'
_o='cipTcpPassiveOpens'
_n='cipTcpActiveOpens'
_m='cipTcpMaxConn'
_l='cipTcpRtoMax'
_k='cipTcpRtoMin'
_j='cipTcpRtoAlgorithm'
_i='cipIpRoutingDiscards'
_h='cipIpFragCreates'
_g='cipIpFragFails'
_f='cipIpFragOKs'
_e='cipIpReasmFails'
_d='cipIpReasmOKs'
_c='cipIpReasmReqds'
_b='cipIpReasmTimeout'
_a='cipIpOutNoRoutes'
_Z='cipIpOutDiscards'
_Y='cipIpOutRequests'
_X='cipIpInDelivers'
_W='cipIpInDiscards'
_V='cipIpInUnknownProtos'
_U='cipIpForwDatagrams'
_T='cipIpInAddrErrors'
_S='cipIpInHdrErrors'
_R='cipIpInReceives'
_Q='cipIpDefaultTTL'
_P='cipIpForwarding'
_O='cipTcpConnRemPort'
_N='cipTcpConnRemAddress'
_M='cipTcpConnLocalPort'
_L='milliseconds'
_K='cipUdpLocalPort'
_J='read-write'
_I='octets'
_H='not-accessible'
_G='cipIpAddress'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='CISCO-CIPTCPIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCipTcpIpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,32))
if mibBuilder.loadTexts:ciscoCipTcpIpMIB.setRevisions(('1998-01-06 00:00','1995-08-21 00:00','1995-04-28 00:00'))
_CipTcpIpObjects_ObjectIdentity=ObjectIdentity
cipTcpIpObjects=_CipTcpIpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,32,1))
_CipIpObjects_ObjectIdentity=ObjectIdentity
cipIpObjects=_CipIpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,32,1,1))
_CipIpTable_Object=MibTable
cipIpTable=_CipIpTable_Object((1,3,6,1,4,1,9,9,32,1,1,1))
if mibBuilder.loadTexts:cipIpTable.setStatus(_A)
_CipIpEntry_Object=MibTableRow
cipIpEntry=_CipIpEntry_Object((1,3,6,1,4,1,9,9,32,1,1,1,1))
cipIpEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:cipIpEntry.setStatus(_A)
_CipIpAddress_Type=IpAddress
_CipIpAddress_Object=MibTableColumn
cipIpAddress=_CipIpAddress_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,1),_CipIpAddress_Type())
cipIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cipIpAddress.setStatus(_A)
class _CipIpForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('notForwarding',2)))
_CipIpForwarding_Type.__name__=_D
_CipIpForwarding_Object=MibTableColumn
cipIpForwarding=_CipIpForwarding_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,2),_CipIpForwarding_Type())
cipIpForwarding.setMaxAccess(_J)
if mibBuilder.loadTexts:cipIpForwarding.setStatus(_A)
class _CipIpDefaultTTL_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CipIpDefaultTTL_Type.__name__=_D
_CipIpDefaultTTL_Object=MibTableColumn
cipIpDefaultTTL=_CipIpDefaultTTL_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,3),_CipIpDefaultTTL_Type())
cipIpDefaultTTL.setMaxAccess(_J)
if mibBuilder.loadTexts:cipIpDefaultTTL.setStatus(_A)
_CipIpInReceives_Type=Counter32
_CipIpInReceives_Object=MibTableColumn
cipIpInReceives=_CipIpInReceives_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,4),_CipIpInReceives_Type())
cipIpInReceives.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpInReceives.setStatus(_A)
_CipIpInHdrErrors_Type=Counter32
_CipIpInHdrErrors_Object=MibTableColumn
cipIpInHdrErrors=_CipIpInHdrErrors_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,5),_CipIpInHdrErrors_Type())
cipIpInHdrErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpInHdrErrors.setStatus(_A)
_CipIpInAddrErrors_Type=Counter32
_CipIpInAddrErrors_Object=MibTableColumn
cipIpInAddrErrors=_CipIpInAddrErrors_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,6),_CipIpInAddrErrors_Type())
cipIpInAddrErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpInAddrErrors.setStatus(_A)
_CipIpForwDatagrams_Type=Counter32
_CipIpForwDatagrams_Object=MibTableColumn
cipIpForwDatagrams=_CipIpForwDatagrams_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,7),_CipIpForwDatagrams_Type())
cipIpForwDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpForwDatagrams.setStatus(_A)
_CipIpInUnknownProtos_Type=Counter32
_CipIpInUnknownProtos_Object=MibTableColumn
cipIpInUnknownProtos=_CipIpInUnknownProtos_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,8),_CipIpInUnknownProtos_Type())
cipIpInUnknownProtos.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpInUnknownProtos.setStatus(_A)
_CipIpInDiscards_Type=Counter32
_CipIpInDiscards_Object=MibTableColumn
cipIpInDiscards=_CipIpInDiscards_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,9),_CipIpInDiscards_Type())
cipIpInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpInDiscards.setStatus(_A)
_CipIpInDelivers_Type=Counter32
_CipIpInDelivers_Object=MibTableColumn
cipIpInDelivers=_CipIpInDelivers_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,10),_CipIpInDelivers_Type())
cipIpInDelivers.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpInDelivers.setStatus(_A)
_CipIpOutRequests_Type=Counter32
_CipIpOutRequests_Object=MibTableColumn
cipIpOutRequests=_CipIpOutRequests_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,11),_CipIpOutRequests_Type())
cipIpOutRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpOutRequests.setStatus(_A)
_CipIpOutDiscards_Type=Counter32
_CipIpOutDiscards_Object=MibTableColumn
cipIpOutDiscards=_CipIpOutDiscards_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,12),_CipIpOutDiscards_Type())
cipIpOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpOutDiscards.setStatus(_A)
_CipIpOutNoRoutes_Type=Counter32
_CipIpOutNoRoutes_Object=MibTableColumn
cipIpOutNoRoutes=_CipIpOutNoRoutes_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,13),_CipIpOutNoRoutes_Type())
cipIpOutNoRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpOutNoRoutes.setStatus(_A)
_CipIpReasmTimeout_Type=Integer32
_CipIpReasmTimeout_Object=MibTableColumn
cipIpReasmTimeout=_CipIpReasmTimeout_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,14),_CipIpReasmTimeout_Type())
cipIpReasmTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpReasmTimeout.setStatus(_A)
_CipIpReasmReqds_Type=Counter32
_CipIpReasmReqds_Object=MibTableColumn
cipIpReasmReqds=_CipIpReasmReqds_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,15),_CipIpReasmReqds_Type())
cipIpReasmReqds.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpReasmReqds.setStatus(_A)
_CipIpReasmOKs_Type=Counter32
_CipIpReasmOKs_Object=MibTableColumn
cipIpReasmOKs=_CipIpReasmOKs_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,16),_CipIpReasmOKs_Type())
cipIpReasmOKs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpReasmOKs.setStatus(_A)
_CipIpReasmFails_Type=Counter32
_CipIpReasmFails_Object=MibTableColumn
cipIpReasmFails=_CipIpReasmFails_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,17),_CipIpReasmFails_Type())
cipIpReasmFails.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpReasmFails.setStatus(_A)
_CipIpFragOKs_Type=Counter32
_CipIpFragOKs_Object=MibTableColumn
cipIpFragOKs=_CipIpFragOKs_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,18),_CipIpFragOKs_Type())
cipIpFragOKs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpFragOKs.setStatus(_A)
_CipIpFragFails_Type=Counter32
_CipIpFragFails_Object=MibTableColumn
cipIpFragFails=_CipIpFragFails_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,19),_CipIpFragFails_Type())
cipIpFragFails.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpFragFails.setStatus(_A)
_CipIpFragCreates_Type=Counter32
_CipIpFragCreates_Object=MibTableColumn
cipIpFragCreates=_CipIpFragCreates_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,20),_CipIpFragCreates_Type())
cipIpFragCreates.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpFragCreates.setStatus(_A)
_CipIpRoutingDiscards_Type=Counter32
_CipIpRoutingDiscards_Object=MibTableColumn
cipIpRoutingDiscards=_CipIpRoutingDiscards_Object((1,3,6,1,4,1,9,9,32,1,1,1,1,21),_CipIpRoutingDiscards_Type())
cipIpRoutingDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIpRoutingDiscards.setStatus(_A)
_CipTcpObjects_ObjectIdentity=ObjectIdentity
cipTcpObjects=_CipTcpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,32,1,2))
_CipTcpStackTable_Object=MibTable
cipTcpStackTable=_CipTcpStackTable_Object((1,3,6,1,4,1,9,9,32,1,2,1))
if mibBuilder.loadTexts:cipTcpStackTable.setStatus(_A)
_CipTcpStackEntry_Object=MibTableRow
cipTcpStackEntry=_CipTcpStackEntry_Object((1,3,6,1,4,1,9,9,32,1,2,1,1))
cipTcpStackEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:cipTcpStackEntry.setStatus(_A)
class _CipTcpRtoAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('constant',2),('rsre',3),('vanj',4)))
_CipTcpRtoAlgorithm_Type.__name__=_D
_CipTcpRtoAlgorithm_Object=MibTableColumn
cipTcpRtoAlgorithm=_CipTcpRtoAlgorithm_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,1),_CipTcpRtoAlgorithm_Type())
cipTcpRtoAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpRtoAlgorithm.setStatus(_A)
_CipTcpRtoMin_Type=Integer32
_CipTcpRtoMin_Object=MibTableColumn
cipTcpRtoMin=_CipTcpRtoMin_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,2),_CipTcpRtoMin_Type())
cipTcpRtoMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpRtoMin.setStatus(_A)
if mibBuilder.loadTexts:cipTcpRtoMin.setUnits(_L)
_CipTcpRtoMax_Type=Integer32
_CipTcpRtoMax_Object=MibTableColumn
cipTcpRtoMax=_CipTcpRtoMax_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,3),_CipTcpRtoMax_Type())
cipTcpRtoMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpRtoMax.setStatus(_A)
if mibBuilder.loadTexts:cipTcpRtoMax.setUnits(_L)
_CipTcpMaxConn_Type=Integer32
_CipTcpMaxConn_Object=MibTableColumn
cipTcpMaxConn=_CipTcpMaxConn_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,4),_CipTcpMaxConn_Type())
cipTcpMaxConn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpMaxConn.setStatus(_A)
_CipTcpActiveOpens_Type=Counter32
_CipTcpActiveOpens_Object=MibTableColumn
cipTcpActiveOpens=_CipTcpActiveOpens_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,5),_CipTcpActiveOpens_Type())
cipTcpActiveOpens.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpActiveOpens.setStatus(_A)
_CipTcpPassiveOpens_Type=Counter32
_CipTcpPassiveOpens_Object=MibTableColumn
cipTcpPassiveOpens=_CipTcpPassiveOpens_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,6),_CipTcpPassiveOpens_Type())
cipTcpPassiveOpens.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpPassiveOpens.setStatus(_A)
_CipTcpAttemptFails_Type=Counter32
_CipTcpAttemptFails_Object=MibTableColumn
cipTcpAttemptFails=_CipTcpAttemptFails_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,7),_CipTcpAttemptFails_Type())
cipTcpAttemptFails.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpAttemptFails.setStatus(_A)
_CipTcpEstabResets_Type=Counter32
_CipTcpEstabResets_Object=MibTableColumn
cipTcpEstabResets=_CipTcpEstabResets_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,8),_CipTcpEstabResets_Type())
cipTcpEstabResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpEstabResets.setStatus(_A)
_CipTcpCurrEstab_Type=Gauge32
_CipTcpCurrEstab_Object=MibTableColumn
cipTcpCurrEstab=_CipTcpCurrEstab_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,9),_CipTcpCurrEstab_Type())
cipTcpCurrEstab.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpCurrEstab.setStatus(_A)
_CipTcpInSegs_Type=Counter32
_CipTcpInSegs_Object=MibTableColumn
cipTcpInSegs=_CipTcpInSegs_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,10),_CipTcpInSegs_Type())
cipTcpInSegs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpInSegs.setStatus(_A)
_CipTcpOutSegs_Type=Counter32
_CipTcpOutSegs_Object=MibTableColumn
cipTcpOutSegs=_CipTcpOutSegs_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,11),_CipTcpOutSegs_Type())
cipTcpOutSegs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpOutSegs.setStatus(_A)
_CipTcpRetransSegs_Type=Counter32
_CipTcpRetransSegs_Object=MibTableColumn
cipTcpRetransSegs=_CipTcpRetransSegs_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,12),_CipTcpRetransSegs_Type())
cipTcpRetransSegs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpRetransSegs.setStatus(_A)
_CipTcpInErrs_Type=Counter32
_CipTcpInErrs_Object=MibTableColumn
cipTcpInErrs=_CipTcpInErrs_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,13),_CipTcpInErrs_Type())
cipTcpInErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpInErrs.setStatus(_A)
_CipTcpOutRsts_Type=Counter32
_CipTcpOutRsts_Object=MibTableColumn
cipTcpOutRsts=_CipTcpOutRsts_Object((1,3,6,1,4,1,9,9,32,1,2,1,1,14),_CipTcpOutRsts_Type())
cipTcpOutRsts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpOutRsts.setStatus(_A)
_CipTcpConnTable_Object=MibTable
cipTcpConnTable=_CipTcpConnTable_Object((1,3,6,1,4,1,9,9,32,1,2,2))
if mibBuilder.loadTexts:cipTcpConnTable.setStatus(_A)
_CipTcpConnEntry_Object=MibTableRow
cipTcpConnEntry=_CipTcpConnEntry_Object((1,3,6,1,4,1,9,9,32,1,2,2,1))
cipTcpConnEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:cipTcpConnEntry.setStatus(_A)
class _CipTcpConnLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CipTcpConnLocalPort_Type.__name__=_D
_CipTcpConnLocalPort_Object=MibTableColumn
cipTcpConnLocalPort=_CipTcpConnLocalPort_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,1),_CipTcpConnLocalPort_Type())
cipTcpConnLocalPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cipTcpConnLocalPort.setStatus(_A)
_CipTcpConnRemAddress_Type=IpAddress
_CipTcpConnRemAddress_Object=MibTableColumn
cipTcpConnRemAddress=_CipTcpConnRemAddress_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,2),_CipTcpConnRemAddress_Type())
cipTcpConnRemAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cipTcpConnRemAddress.setStatus(_A)
class _CipTcpConnRemPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CipTcpConnRemPort_Type.__name__=_D
_CipTcpConnRemPort_Object=MibTableColumn
cipTcpConnRemPort=_CipTcpConnRemPort_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,3),_CipTcpConnRemPort_Type())
cipTcpConnRemPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cipTcpConnRemPort.setStatus(_A)
class _CipTcpConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('closed',1),('listen',2),('synSent',3),('synReceived',4),('established',5),('finWait1',6),('finWait2',7),('closeWait',8),('lastAck',9),('closing',10),('timeWait',11),('deleteTCB',12)))
_CipTcpConnState_Type.__name__=_D
_CipTcpConnState_Object=MibTableColumn
cipTcpConnState=_CipTcpConnState_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,4),_CipTcpConnState_Type())
cipTcpConnState.setMaxAccess(_J)
if mibBuilder.loadTexts:cipTcpConnState.setStatus(_A)
_CipTcpConnInHCBytes_Type=Counter64
_CipTcpConnInHCBytes_Object=MibTableColumn
cipTcpConnInHCBytes=_CipTcpConnInHCBytes_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,5),_CipTcpConnInHCBytes_Type())
cipTcpConnInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpConnInHCBytes.setStatus(_A)
if mibBuilder.loadTexts:cipTcpConnInHCBytes.setUnits(_I)
_CipTcpConnInBytes_Type=Counter32
_CipTcpConnInBytes_Object=MibTableColumn
cipTcpConnInBytes=_CipTcpConnInBytes_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,6),_CipTcpConnInBytes_Type())
cipTcpConnInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpConnInBytes.setStatus(_A)
if mibBuilder.loadTexts:cipTcpConnInBytes.setUnits(_I)
_CipTcpConnOutHCBytes_Type=Counter64
_CipTcpConnOutHCBytes_Object=MibTableColumn
cipTcpConnOutHCBytes=_CipTcpConnOutHCBytes_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,7),_CipTcpConnOutHCBytes_Type())
cipTcpConnOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpConnOutHCBytes.setStatus(_A)
if mibBuilder.loadTexts:cipTcpConnOutHCBytes.setUnits(_I)
_CipTcpConnOutBytes_Type=Counter32
_CipTcpConnOutBytes_Object=MibTableColumn
cipTcpConnOutBytes=_CipTcpConnOutBytes_Object((1,3,6,1,4,1,9,9,32,1,2,2,1,8),_CipTcpConnOutBytes_Type())
cipTcpConnOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTcpConnOutBytes.setStatus(_A)
if mibBuilder.loadTexts:cipTcpConnOutBytes.setUnits(_I)
_CipIcmpObjects_ObjectIdentity=ObjectIdentity
cipIcmpObjects=_CipIcmpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,32,1,3))
_CipIcmpTable_Object=MibTable
cipIcmpTable=_CipIcmpTable_Object((1,3,6,1,4,1,9,9,32,1,3,1))
if mibBuilder.loadTexts:cipIcmpTable.setStatus(_A)
_CipIcmpEntry_Object=MibTableRow
cipIcmpEntry=_CipIcmpEntry_Object((1,3,6,1,4,1,9,9,32,1,3,1,1))
cipIcmpEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:cipIcmpEntry.setStatus(_A)
_CipIcmpInMsgs_Type=Counter32
_CipIcmpInMsgs_Object=MibTableColumn
cipIcmpInMsgs=_CipIcmpInMsgs_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,1),_CipIcmpInMsgs_Type())
cipIcmpInMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInMsgs.setStatus(_A)
_CipIcmpInErrors_Type=Counter32
_CipIcmpInErrors_Object=MibTableColumn
cipIcmpInErrors=_CipIcmpInErrors_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,2),_CipIcmpInErrors_Type())
cipIcmpInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInErrors.setStatus(_A)
_CipIcmpInDestUnreachs_Type=Counter32
_CipIcmpInDestUnreachs_Object=MibTableColumn
cipIcmpInDestUnreachs=_CipIcmpInDestUnreachs_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,3),_CipIcmpInDestUnreachs_Type())
cipIcmpInDestUnreachs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInDestUnreachs.setStatus(_A)
_CipIcmpInTimeExcds_Type=Counter32
_CipIcmpInTimeExcds_Object=MibTableColumn
cipIcmpInTimeExcds=_CipIcmpInTimeExcds_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,4),_CipIcmpInTimeExcds_Type())
cipIcmpInTimeExcds.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInTimeExcds.setStatus(_A)
_CipIcmpInParmProbs_Type=Counter32
_CipIcmpInParmProbs_Object=MibTableColumn
cipIcmpInParmProbs=_CipIcmpInParmProbs_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,5),_CipIcmpInParmProbs_Type())
cipIcmpInParmProbs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInParmProbs.setStatus(_A)
_CipIcmpInSrcQuenchs_Type=Counter32
_CipIcmpInSrcQuenchs_Object=MibTableColumn
cipIcmpInSrcQuenchs=_CipIcmpInSrcQuenchs_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,6),_CipIcmpInSrcQuenchs_Type())
cipIcmpInSrcQuenchs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInSrcQuenchs.setStatus(_A)
_CipIcmpInRedirects_Type=Counter32
_CipIcmpInRedirects_Object=MibTableColumn
cipIcmpInRedirects=_CipIcmpInRedirects_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,7),_CipIcmpInRedirects_Type())
cipIcmpInRedirects.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInRedirects.setStatus(_A)
_CipIcmpInEchos_Type=Counter32
_CipIcmpInEchos_Object=MibTableColumn
cipIcmpInEchos=_CipIcmpInEchos_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,8),_CipIcmpInEchos_Type())
cipIcmpInEchos.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInEchos.setStatus(_A)
_CipIcmpInAddrMaskReps_Type=Counter32
_CipIcmpInAddrMaskReps_Object=MibTableColumn
cipIcmpInAddrMaskReps=_CipIcmpInAddrMaskReps_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,9),_CipIcmpInAddrMaskReps_Type())
cipIcmpInAddrMaskReps.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpInAddrMaskReps.setStatus(_A)
_CipIcmpOutMsgs_Type=Counter32
_CipIcmpOutMsgs_Object=MibTableColumn
cipIcmpOutMsgs=_CipIcmpOutMsgs_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,10),_CipIcmpOutMsgs_Type())
cipIcmpOutMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutMsgs.setStatus(_A)
_CipIcmpOutErrors_Type=Counter32
_CipIcmpOutErrors_Object=MibTableColumn
cipIcmpOutErrors=_CipIcmpOutErrors_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,11),_CipIcmpOutErrors_Type())
cipIcmpOutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutErrors.setStatus(_A)
_CipIcmpOutDestUnreachs_Type=Counter32
_CipIcmpOutDestUnreachs_Object=MibTableColumn
cipIcmpOutDestUnreachs=_CipIcmpOutDestUnreachs_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,12),_CipIcmpOutDestUnreachs_Type())
cipIcmpOutDestUnreachs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutDestUnreachs.setStatus(_A)
_CipIcmpOutEchos_Type=Counter32
_CipIcmpOutEchos_Object=MibTableColumn
cipIcmpOutEchos=_CipIcmpOutEchos_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,13),_CipIcmpOutEchos_Type())
cipIcmpOutEchos.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutEchos.setStatus(_A)
_CipIcmpOutEchoReps_Type=Counter32
_CipIcmpOutEchoReps_Object=MibTableColumn
cipIcmpOutEchoReps=_CipIcmpOutEchoReps_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,14),_CipIcmpOutEchoReps_Type())
cipIcmpOutEchoReps.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutEchoReps.setStatus(_A)
_CipIcmpOutTimestamps_Type=Counter32
_CipIcmpOutTimestamps_Object=MibTableColumn
cipIcmpOutTimestamps=_CipIcmpOutTimestamps_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,15),_CipIcmpOutTimestamps_Type())
cipIcmpOutTimestamps.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutTimestamps.setStatus(_A)
_CipIcmpOutTimestampReps_Type=Counter32
_CipIcmpOutTimestampReps_Object=MibTableColumn
cipIcmpOutTimestampReps=_CipIcmpOutTimestampReps_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,16),_CipIcmpOutTimestampReps_Type())
cipIcmpOutTimestampReps.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutTimestampReps.setStatus(_A)
_CipIcmpOutAddrMasks_Type=Counter32
_CipIcmpOutAddrMasks_Object=MibTableColumn
cipIcmpOutAddrMasks=_CipIcmpOutAddrMasks_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,17),_CipIcmpOutAddrMasks_Type())
cipIcmpOutAddrMasks.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutAddrMasks.setStatus(_A)
_CipIcmpOutAddrMaskReps_Type=Counter32
_CipIcmpOutAddrMaskReps_Object=MibTableColumn
cipIcmpOutAddrMaskReps=_CipIcmpOutAddrMaskReps_Object((1,3,6,1,4,1,9,9,32,1,3,1,1,18),_CipIcmpOutAddrMaskReps_Type())
cipIcmpOutAddrMaskReps.setMaxAccess(_C)
if mibBuilder.loadTexts:cipIcmpOutAddrMaskReps.setStatus(_A)
_CipUdpObjects_ObjectIdentity=ObjectIdentity
cipUdpObjects=_CipUdpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,32,1,4))
_CipUdpTable_Object=MibTable
cipUdpTable=_CipUdpTable_Object((1,3,6,1,4,1,9,9,32,1,4,1))
if mibBuilder.loadTexts:cipUdpTable.setStatus(_A)
_CipUdpEntry_Object=MibTableRow
cipUdpEntry=_CipUdpEntry_Object((1,3,6,1,4,1,9,9,32,1,4,1,1))
cipUdpEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:cipUdpEntry.setStatus(_A)
_CipUdpInDatagrams_Type=Counter32
_CipUdpInDatagrams_Object=MibTableColumn
cipUdpInDatagrams=_CipUdpInDatagrams_Object((1,3,6,1,4,1,9,9,32,1,4,1,1,1),_CipUdpInDatagrams_Type())
cipUdpInDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUdpInDatagrams.setStatus(_A)
_CipUdpNoPorts_Type=Counter32
_CipUdpNoPorts_Object=MibTableColumn
cipUdpNoPorts=_CipUdpNoPorts_Object((1,3,6,1,4,1,9,9,32,1,4,1,1,2),_CipUdpNoPorts_Type())
cipUdpNoPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUdpNoPorts.setStatus(_A)
_CipUdpInErrors_Type=Counter32
_CipUdpInErrors_Object=MibTableColumn
cipUdpInErrors=_CipUdpInErrors_Object((1,3,6,1,4,1,9,9,32,1,4,1,1,3),_CipUdpInErrors_Type())
cipUdpInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUdpInErrors.setStatus(_A)
_CipUdpOutDatagrams_Type=Counter32
_CipUdpOutDatagrams_Object=MibTableColumn
cipUdpOutDatagrams=_CipUdpOutDatagrams_Object((1,3,6,1,4,1,9,9,32,1,4,1,1,4),_CipUdpOutDatagrams_Type())
cipUdpOutDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUdpOutDatagrams.setStatus(_A)
_CipUdpListenersTable_Object=MibTable
cipUdpListenersTable=_CipUdpListenersTable_Object((1,3,6,1,4,1,9,9,32,1,4,2))
if mibBuilder.loadTexts:cipUdpListenersTable.setStatus(_A)
_CipUdpListenersEntry_Object=MibTableRow
cipUdpListenersEntry=_CipUdpListenersEntry_Object((1,3,6,1,4,1,9,9,32,1,4,2,1))
cipUdpListenersEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_K))
if mibBuilder.loadTexts:cipUdpListenersEntry.setStatus(_A)
class _CipUdpLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CipUdpLocalPort_Type.__name__=_D
_CipUdpLocalPort_Object=MibTableColumn
cipUdpLocalPort=_CipUdpLocalPort_Object((1,3,6,1,4,1,9,9,32,1,4,2,1,1),_CipUdpLocalPort_Type())
cipUdpLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUdpLocalPort.setStatus(_A)
_CiscoCipTcpIpMibConformance_ObjectIdentity=ObjectIdentity
ciscoCipTcpIpMibConformance=_CiscoCipTcpIpMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,32,2))
_CiscoCipTcpIpMibCompliances_ObjectIdentity=ObjectIdentity
ciscoCipTcpIpMibCompliances=_CiscoCipTcpIpMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,32,2,1))
_CiscoCipTcpIpMibGroups_ObjectIdentity=ObjectIdentity
ciscoCipTcpIpMibGroups=_CiscoCipTcpIpMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,32,2,2))
ciscoCipTcpIpGroup=ObjectGroup((1,3,6,1,4,1,9,9,32,2,2,1))
ciscoCipTcpIpGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_K)))
if mibBuilder.loadTexts:ciscoCipTcpIpGroup.setStatus(_A)
ciscoCipTcpIpMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,32,2,1,1))
ciscoCipTcpIpMibCompliance.setObjects((_B,_AO))
if mibBuilder.loadTexts:ciscoCipTcpIpMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCipTcpIpMIB':ciscoCipTcpIpMIB,'cipTcpIpObjects':cipTcpIpObjects,'cipIpObjects':cipIpObjects,'cipIpTable':cipIpTable,'cipIpEntry':cipIpEntry,_G:cipIpAddress,_P:cipIpForwarding,_Q:cipIpDefaultTTL,_R:cipIpInReceives,_S:cipIpInHdrErrors,_T:cipIpInAddrErrors,_U:cipIpForwDatagrams,_V:cipIpInUnknownProtos,_W:cipIpInDiscards,_X:cipIpInDelivers,_Y:cipIpOutRequests,_Z:cipIpOutDiscards,_a:cipIpOutNoRoutes,_b:cipIpReasmTimeout,_c:cipIpReasmReqds,_d:cipIpReasmOKs,_e:cipIpReasmFails,_f:cipIpFragOKs,_g:cipIpFragFails,_h:cipIpFragCreates,_i:cipIpRoutingDiscards,'cipTcpObjects':cipTcpObjects,'cipTcpStackTable':cipTcpStackTable,'cipTcpStackEntry':cipTcpStackEntry,_j:cipTcpRtoAlgorithm,_k:cipTcpRtoMin,_l:cipTcpRtoMax,_m:cipTcpMaxConn,_n:cipTcpActiveOpens,_o:cipTcpPassiveOpens,_p:cipTcpAttemptFails,_q:cipTcpEstabResets,_r:cipTcpCurrEstab,_s:cipTcpInSegs,_t:cipTcpOutSegs,_u:cipTcpRetransSegs,_v:cipTcpInErrs,_w:cipTcpOutRsts,'cipTcpConnTable':cipTcpConnTable,'cipTcpConnEntry':cipTcpConnEntry,_M:cipTcpConnLocalPort,_N:cipTcpConnRemAddress,_O:cipTcpConnRemPort,_x:cipTcpConnState,_z:cipTcpConnInHCBytes,_y:cipTcpConnInBytes,_A1:cipTcpConnOutHCBytes,_A0:cipTcpConnOutBytes,'cipIcmpObjects':cipIcmpObjects,'cipIcmpTable':cipIcmpTable,'cipIcmpEntry':cipIcmpEntry,_A2:cipIcmpInMsgs,_A3:cipIcmpInErrors,_A4:cipIcmpInDestUnreachs,_A5:cipIcmpInTimeExcds,_A6:cipIcmpInParmProbs,_A7:cipIcmpInSrcQuenchs,_A8:cipIcmpInRedirects,_A9:cipIcmpInEchos,_AA:cipIcmpInAddrMaskReps,_AB:cipIcmpOutMsgs,_AC:cipIcmpOutErrors,_AD:cipIcmpOutDestUnreachs,_AE:cipIcmpOutEchos,_AF:cipIcmpOutEchoReps,_AG:cipIcmpOutTimestamps,_AH:cipIcmpOutTimestampReps,_AI:cipIcmpOutAddrMasks,_AJ:cipIcmpOutAddrMaskReps,'cipUdpObjects':cipUdpObjects,'cipUdpTable':cipUdpTable,'cipUdpEntry':cipUdpEntry,_AK:cipUdpInDatagrams,_AL:cipUdpNoPorts,_AM:cipUdpInErrors,_AN:cipUdpOutDatagrams,'cipUdpListenersTable':cipUdpListenersTable,'cipUdpListenersEntry':cipUdpListenersEntry,_K:cipUdpLocalPort,'ciscoCipTcpIpMibConformance':ciscoCipTcpIpMibConformance,'ciscoCipTcpIpMibCompliances':ciscoCipTcpIpMibCompliances,'ciscoCipTcpIpMibCompliance':ciscoCipTcpIpMibCompliance,'ciscoCipTcpIpMibGroups':ciscoCipTcpIpMibGroups,_AO:ciscoCipTcpIpGroup})