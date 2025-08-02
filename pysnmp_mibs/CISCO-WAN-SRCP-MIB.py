_p='srcpConfigurationGroup3'
_o='srcpConfigurationGroup2'
_n='srcpStatisticsGroup'
_m='srcpConfigurationGroup'
_l='srcpPeerGrpMaxPduSize'
_k='srcpPeerGrpTimeSinceHeartbeat'
_j='srcpPeerGrpHeartbeatInterval'
_i='srcpStatsPeerIpAddress'
_h='octets'
_g='not-accessible'
_f='srcpPeerId'
_e='mgcRedundancyGrpNum'
_d='CISCO-WAN-MGC-REDUN-MIB'
_c='srcpStatisticsGroup2'
_b='srcpRequestMaxTimeout'
_a='srcpRequestRetries'
_Z='srcpRequestTimeOut'
_Y='ntfyFailCnts'
_X='rqntFailCnts'
_W='aulnFailCnts'
_V='augwFailCnts'
_U='ntfyCnts'
_T='rqntCnts'
_S='aulnCnts'
_R='augwCnts'
_Q='packetsDiscardedCnts'
_P='srcpStatsPeerName'
_O='srcpPeerMaxPduSize'
_N='srcpPeerTimeSinceHeartbeat'
_M='srcpPeerHeartbeatInterval'
_L='srcpPeerPortNumber'
_K='srcpPeerName'
_J='srcpPortNumber'
_I='srcpVersion'
_H='DisplayString'
_G='milliseconds'
_F='deprecated'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-WAN-SRCP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mgcRedundancyGrpNum,=mibBuilder.importSymbols(_d,_e)
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
ciscoWanSrcpMIB=ModuleIdentity((1,3,6,1,4,1,351,150,11))
if mibBuilder.loadTexts:ciscoWanSrcpMIB.setRevisions(('2004-01-30 00:00','2000-12-26 00:00','2000-08-31 00:00','2000-07-21 00:00','2000-05-28 00:00','2000-05-24 00:00','1999-11-23 00:00','1999-11-01 00:00','1999-10-21 00:00','1999-06-23 00:00','1999-06-07 00:00','1999-04-29 00:00'))
_SrcpObjects_ObjectIdentity=ObjectIdentity
srcpObjects=_SrcpObjects_ObjectIdentity((1,3,6,1,4,1,351,150,11,1))
_SrcpAdminObjects_ObjectIdentity=ObjectIdentity
srcpAdminObjects=_SrcpAdminObjects_ObjectIdentity((1,3,6,1,4,1,351,150,11,1,1))
class _SrcpVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SrcpVersion_Type.__name__=_H
_SrcpVersion_Object=MibScalar
srcpVersion=_SrcpVersion_Object((1,3,6,1,4,1,351,150,11,1,1,1),_SrcpVersion_Type())
srcpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:srcpVersion.setStatus(_B)
class _SrcpPortNumber_Type(Integer32):defaultValue=2428;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SrcpPortNumber_Type.__name__=_D
_SrcpPortNumber_Object=MibScalar
srcpPortNumber=_SrcpPortNumber_Object((1,3,6,1,4,1,351,150,11,1,1,2),_SrcpPortNumber_Type())
srcpPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpPortNumber.setStatus(_B)
_SrcpPeerTable_Object=MibTable
srcpPeerTable=_SrcpPeerTable_Object((1,3,6,1,4,1,351,150,11,1,1,3))
if mibBuilder.loadTexts:srcpPeerTable.setStatus(_B)
_SrcpPeerEntry_Object=MibTableRow
srcpPeerEntry=_SrcpPeerEntry_Object((1,3,6,1,4,1,351,150,11,1,1,3,1))
srcpPeerEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:srcpPeerEntry.setStatus(_B)
class _SrcpPeerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SrcpPeerId_Type.__name__=_D
_SrcpPeerId_Object=MibTableColumn
srcpPeerId=_SrcpPeerId_Object((1,3,6,1,4,1,351,150,11,1,1,3,1,1),_SrcpPeerId_Type())
srcpPeerId.setMaxAccess(_g)
if mibBuilder.loadTexts:srcpPeerId.setStatus(_B)
class _SrcpPeerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SrcpPeerName_Type.__name__=_H
_SrcpPeerName_Object=MibTableColumn
srcpPeerName=_SrcpPeerName_Object((1,3,6,1,4,1,351,150,11,1,1,3,1,2),_SrcpPeerName_Type())
srcpPeerName.setMaxAccess(_C)
if mibBuilder.loadTexts:srcpPeerName.setStatus(_B)
class _SrcpPeerPortNumber_Type(Integer32):defaultValue=2428;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SrcpPeerPortNumber_Type.__name__=_D
_SrcpPeerPortNumber_Object=MibTableColumn
srcpPeerPortNumber=_SrcpPeerPortNumber_Object((1,3,6,1,4,1,351,150,11,1,1,3,1,3),_SrcpPeerPortNumber_Type())
srcpPeerPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpPeerPortNumber.setStatus(_B)
class _SrcpPeerHeartbeatInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SrcpPeerHeartbeatInterval_Type.__name__=_D
_SrcpPeerHeartbeatInterval_Object=MibTableColumn
srcpPeerHeartbeatInterval=_SrcpPeerHeartbeatInterval_Object((1,3,6,1,4,1,351,150,11,1,1,3,1,4),_SrcpPeerHeartbeatInterval_Type())
srcpPeerHeartbeatInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpPeerHeartbeatInterval.setStatus(_F)
if mibBuilder.loadTexts:srcpPeerHeartbeatInterval.setUnits(_G)
class _SrcpPeerTimeSinceHeartbeat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SrcpPeerTimeSinceHeartbeat_Type.__name__=_D
_SrcpPeerTimeSinceHeartbeat_Object=MibTableColumn
srcpPeerTimeSinceHeartbeat=_SrcpPeerTimeSinceHeartbeat_Object((1,3,6,1,4,1,351,150,11,1,1,3,1,5),_SrcpPeerTimeSinceHeartbeat_Type())
srcpPeerTimeSinceHeartbeat.setMaxAccess(_C)
if mibBuilder.loadTexts:srcpPeerTimeSinceHeartbeat.setStatus(_F)
if mibBuilder.loadTexts:srcpPeerTimeSinceHeartbeat.setUnits(_G)
class _SrcpPeerMaxPduSize_Type(Integer32):defaultValue=16384;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4095,65535))
_SrcpPeerMaxPduSize_Type.__name__=_D
_SrcpPeerMaxPduSize_Object=MibTableColumn
srcpPeerMaxPduSize=_SrcpPeerMaxPduSize_Object((1,3,6,1,4,1,351,150,11,1,1,3,1,6),_SrcpPeerMaxPduSize_Type())
srcpPeerMaxPduSize.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpPeerMaxPduSize.setStatus(_F)
if mibBuilder.loadTexts:srcpPeerMaxPduSize.setUnits(_h)
_SrcpPeerGrpParamTable_Object=MibTable
srcpPeerGrpParamTable=_SrcpPeerGrpParamTable_Object((1,3,6,1,4,1,351,150,11,1,1,4))
if mibBuilder.loadTexts:srcpPeerGrpParamTable.setStatus(_B)
_SrcpPeerGrpParamEntry_Object=MibTableRow
srcpPeerGrpParamEntry=_SrcpPeerGrpParamEntry_Object((1,3,6,1,4,1,351,150,11,1,1,4,1))
srcpPeerGrpParamEntry.setIndexNames((0,_d,_e))
if mibBuilder.loadTexts:srcpPeerGrpParamEntry.setStatus(_B)
class _SrcpPeerGrpHeartbeatInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SrcpPeerGrpHeartbeatInterval_Type.__name__=_D
_SrcpPeerGrpHeartbeatInterval_Object=MibTableColumn
srcpPeerGrpHeartbeatInterval=_SrcpPeerGrpHeartbeatInterval_Object((1,3,6,1,4,1,351,150,11,1,1,4,1,1),_SrcpPeerGrpHeartbeatInterval_Type())
srcpPeerGrpHeartbeatInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpPeerGrpHeartbeatInterval.setStatus(_B)
if mibBuilder.loadTexts:srcpPeerGrpHeartbeatInterval.setUnits(_G)
class _SrcpPeerGrpTimeSinceHeartbeat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SrcpPeerGrpTimeSinceHeartbeat_Type.__name__=_D
_SrcpPeerGrpTimeSinceHeartbeat_Object=MibTableColumn
srcpPeerGrpTimeSinceHeartbeat=_SrcpPeerGrpTimeSinceHeartbeat_Object((1,3,6,1,4,1,351,150,11,1,1,4,1,2),_SrcpPeerGrpTimeSinceHeartbeat_Type())
srcpPeerGrpTimeSinceHeartbeat.setMaxAccess(_C)
if mibBuilder.loadTexts:srcpPeerGrpTimeSinceHeartbeat.setStatus(_B)
if mibBuilder.loadTexts:srcpPeerGrpTimeSinceHeartbeat.setUnits(_G)
class _SrcpPeerGrpMaxPduSize_Type(Integer32):defaultValue=16384;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4095,65535))
_SrcpPeerGrpMaxPduSize_Type.__name__=_D
_SrcpPeerGrpMaxPduSize_Object=MibTableColumn
srcpPeerGrpMaxPduSize=_SrcpPeerGrpMaxPduSize_Object((1,3,6,1,4,1,351,150,11,1,1,4,1,3),_SrcpPeerGrpMaxPduSize_Type())
srcpPeerGrpMaxPduSize.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpPeerGrpMaxPduSize.setStatus(_B)
if mibBuilder.loadTexts:srcpPeerGrpMaxPduSize.setUnits(_h)
_SrcpStatsObjects_ObjectIdentity=ObjectIdentity
srcpStatsObjects=_SrcpStatsObjects_ObjectIdentity((1,3,6,1,4,1,351,150,11,1,2))
_SrcpPeerStatsTable_Object=MibTable
srcpPeerStatsTable=_SrcpPeerStatsTable_Object((1,3,6,1,4,1,351,150,11,1,2,1))
if mibBuilder.loadTexts:srcpPeerStatsTable.setStatus(_B)
_SrcpPeerStatsEntry_Object=MibTableRow
srcpPeerStatsEntry=_SrcpPeerStatsEntry_Object((1,3,6,1,4,1,351,150,11,1,2,1,1))
srcpPeerStatsEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:srcpPeerStatsEntry.setStatus(_B)
_SrcpStatsPeerIpAddress_Type=IpAddress
_SrcpStatsPeerIpAddress_Object=MibTableColumn
srcpStatsPeerIpAddress=_SrcpStatsPeerIpAddress_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,1),_SrcpStatsPeerIpAddress_Type())
srcpStatsPeerIpAddress.setMaxAccess(_g)
if mibBuilder.loadTexts:srcpStatsPeerIpAddress.setStatus(_B)
class _SrcpStatsPeerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SrcpStatsPeerName_Type.__name__=_H
_SrcpStatsPeerName_Object=MibTableColumn
srcpStatsPeerName=_SrcpStatsPeerName_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,2),_SrcpStatsPeerName_Type())
srcpStatsPeerName.setMaxAccess(_C)
if mibBuilder.loadTexts:srcpStatsPeerName.setStatus(_B)
_PacketsDiscardedCnts_Type=Counter32
_PacketsDiscardedCnts_Object=MibTableColumn
packetsDiscardedCnts=_PacketsDiscardedCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,3),_PacketsDiscardedCnts_Type())
packetsDiscardedCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:packetsDiscardedCnts.setStatus(_B)
_AugwCnts_Type=Counter32
_AugwCnts_Object=MibTableColumn
augwCnts=_AugwCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,4),_AugwCnts_Type())
augwCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:augwCnts.setStatus(_B)
_AulnCnts_Type=Counter32
_AulnCnts_Object=MibTableColumn
aulnCnts=_AulnCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,5),_AulnCnts_Type())
aulnCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:aulnCnts.setStatus(_B)
_RqntCnts_Type=Counter32
_RqntCnts_Object=MibTableColumn
rqntCnts=_RqntCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,6),_RqntCnts_Type())
rqntCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:rqntCnts.setStatus(_B)
_NtfyCnts_Type=Counter32
_NtfyCnts_Object=MibTableColumn
ntfyCnts=_NtfyCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,7),_NtfyCnts_Type())
ntfyCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:ntfyCnts.setStatus(_B)
_AugwFailCnts_Type=Counter32
_AugwFailCnts_Object=MibTableColumn
augwFailCnts=_AugwFailCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,8),_AugwFailCnts_Type())
augwFailCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:augwFailCnts.setStatus(_B)
_AulnFailCnts_Type=Counter32
_AulnFailCnts_Object=MibTableColumn
aulnFailCnts=_AulnFailCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,9),_AulnFailCnts_Type())
aulnFailCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:aulnFailCnts.setStatus(_B)
_RqntFailCnts_Type=Counter32
_RqntFailCnts_Object=MibTableColumn
rqntFailCnts=_RqntFailCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,10),_RqntFailCnts_Type())
rqntFailCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:rqntFailCnts.setStatus(_B)
_NtfyFailCnts_Type=Counter32
_NtfyFailCnts_Object=MibTableColumn
ntfyFailCnts=_NtfyFailCnts_Object((1,3,6,1,4,1,351,150,11,1,2,1,1,11),_NtfyFailCnts_Type())
ntfyFailCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:ntfyFailCnts.setStatus(_B)
_SrcpAdminRetyObjects_ObjectIdentity=ObjectIdentity
srcpAdminRetyObjects=_SrcpAdminRetyObjects_ObjectIdentity((1,3,6,1,4,1,351,150,11,1,3))
class _SrcpRequestTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_SrcpRequestTimeOut_Type.__name__=_D
_SrcpRequestTimeOut_Object=MibScalar
srcpRequestTimeOut=_SrcpRequestTimeOut_Object((1,3,6,1,4,1,351,150,11,1,3,1),_SrcpRequestTimeOut_Type())
srcpRequestTimeOut.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpRequestTimeOut.setStatus(_B)
if mibBuilder.loadTexts:srcpRequestTimeOut.setUnits(_G)
class _SrcpRequestRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SrcpRequestRetries_Type.__name__=_D
_SrcpRequestRetries_Object=MibScalar
srcpRequestRetries=_SrcpRequestRetries_Object((1,3,6,1,4,1,351,150,11,1,3,2),_SrcpRequestRetries_Type())
srcpRequestRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpRequestRetries.setStatus(_B)
class _SrcpRequestMaxTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_SrcpRequestMaxTimeout_Type.__name__=_D
_SrcpRequestMaxTimeout_Object=MibScalar
srcpRequestMaxTimeout=_SrcpRequestMaxTimeout_Object((1,3,6,1,4,1,351,150,11,1,3,3),_SrcpRequestMaxTimeout_Type())
srcpRequestMaxTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:srcpRequestMaxTimeout.setStatus(_B)
if mibBuilder.loadTexts:srcpRequestMaxTimeout.setUnits(_G)
_SrcpMIBConformance_ObjectIdentity=ObjectIdentity
srcpMIBConformance=_SrcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,11,3))
_SrcpMIBCompliances_ObjectIdentity=ObjectIdentity
srcpMIBCompliances=_SrcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,11,3,1))
_SrcpMIBGroups_ObjectIdentity=ObjectIdentity
srcpMIBGroups=_SrcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,11,3,2))
srcpConfigurationGroup=ObjectGroup((1,3,6,1,4,1,351,150,11,3,2,1))
srcpConfigurationGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:srcpConfigurationGroup.setStatus(_F)
srcpStatisticsGroup=ObjectGroup((1,3,6,1,4,1,351,150,11,3,2,2))
srcpStatisticsGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:srcpStatisticsGroup.setStatus(_F)
srcpConfigurationGroup2=ObjectGroup((1,3,6,1,4,1,351,150,11,3,2,3))
srcpConfigurationGroup2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:srcpConfigurationGroup2.setStatus(_F)
srcpStatisticsGroup2=ObjectGroup((1,3,6,1,4,1,351,150,11,3,2,4))
srcpStatisticsGroup2.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:srcpStatisticsGroup2.setStatus(_B)
srcpConfigurationGroup3=ObjectGroup((1,3,6,1,4,1,351,150,11,3,2,5))
srcpConfigurationGroup3.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_j),(_A,_k),(_A,_l),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:srcpConfigurationGroup3.setStatus(_B)
srcpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,11,3,1,1))
srcpMIBCompliance.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:srcpMIBCompliance.setStatus(_F)
srcpMIBComplaince2=ModuleCompliance((1,3,6,1,4,1,351,150,11,3,1,2))
srcpMIBComplaince2.setObjects(*((_A,_o),(_A,_c)))
if mibBuilder.loadTexts:srcpMIBComplaince2.setStatus(_F)
srcpMIBComplaince3=ModuleCompliance((1,3,6,1,4,1,351,150,11,3,1,3))
srcpMIBComplaince3.setObjects(*((_A,_p),(_A,_c)))
if mibBuilder.loadTexts:srcpMIBComplaince3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoWanSrcpMIB':ciscoWanSrcpMIB,'srcpObjects':srcpObjects,'srcpAdminObjects':srcpAdminObjects,_I:srcpVersion,_J:srcpPortNumber,'srcpPeerTable':srcpPeerTable,'srcpPeerEntry':srcpPeerEntry,_f:srcpPeerId,_K:srcpPeerName,_L:srcpPeerPortNumber,_M:srcpPeerHeartbeatInterval,_N:srcpPeerTimeSinceHeartbeat,_O:srcpPeerMaxPduSize,'srcpPeerGrpParamTable':srcpPeerGrpParamTable,'srcpPeerGrpParamEntry':srcpPeerGrpParamEntry,_j:srcpPeerGrpHeartbeatInterval,_k:srcpPeerGrpTimeSinceHeartbeat,_l:srcpPeerGrpMaxPduSize,'srcpStatsObjects':srcpStatsObjects,'srcpPeerStatsTable':srcpPeerStatsTable,'srcpPeerStatsEntry':srcpPeerStatsEntry,_i:srcpStatsPeerIpAddress,_P:srcpStatsPeerName,_Q:packetsDiscardedCnts,_R:augwCnts,_S:aulnCnts,_T:rqntCnts,_U:ntfyCnts,_V:augwFailCnts,_W:aulnFailCnts,_X:rqntFailCnts,_Y:ntfyFailCnts,'srcpAdminRetyObjects':srcpAdminRetyObjects,_Z:srcpRequestTimeOut,_a:srcpRequestRetries,_b:srcpRequestMaxTimeout,'srcpMIBConformance':srcpMIBConformance,'srcpMIBCompliances':srcpMIBCompliances,'srcpMIBCompliance':srcpMIBCompliance,'srcpMIBComplaince2':srcpMIBComplaince2,'srcpMIBComplaince3':srcpMIBComplaince3,'srcpMIBGroups':srcpMIBGroups,_m:srcpConfigurationGroup,_n:srcpStatisticsGroup,_o:srcpConfigurationGroup2,_c:srcpStatisticsGroup2,_p:srcpConfigurationGroup3})