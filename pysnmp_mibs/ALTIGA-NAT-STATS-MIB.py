_v='altigaNatStatsGroup'
_u='alNatAllTranslationPackets'
_t='alNatAllTranslationBytes'
_s='alNatAllTranslationDirection'
_r='alNatAllTranslationAge'
_q='alNatAllTranslationPort'
_p='alNatAllTranslationAddress'
_o='alNatTranslationPackets'
_n='alNatTranslationBytes'
_m='alNatTranslationDirection'
_l='alNatTranslationType'
_k='alNatTranslationAge'
_j='alNatTranslationPort'
_i='alNatTranslationAddress'
_h='alNatStatsMaxTranslations'
_g='alNatStatsActiveTranslations'
_f='alNatStatsTotalTranslations'
_e='alNatStatsPacketsOut'
_d='alNatStatsPacketsIn'
_c='outbound'
_b='inbound'
_a='ilsProxy'
_Z='rasProxy'
_Y='h245Proxy'
_X='h225TcpProxy'
_W='nbdgsvcProxy'
_V='nbnsUdpProxy'
_U='nbnsTcpProxy'
_T='tftpProxy'
_S='ftpProxy'
_R='noPortMap'
_Q='portMapTcpUdp'
_P='portMapUdp'
_O='portMapTcp'
_N='unknown'
_M='alNatAllTranslationType'
_L='alNatAllTranslationDestPort'
_K='alNatAllTranslationDestAddress'
_J='alNatAllTranslationSrcPort'
_I='alNatAllTranslationSrcAddress'
_H='alNatTranslationDestPort'
_G='alNatTranslationDestAddress'
_F='alNatTranslationSrcPort'
_E='alNatTranslationSrcAddress'
_D='Integer32'
_C='read-only'
_B='current'
_A='ALTIGA-NAT-STATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alNatMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alNatMibModule')
alNatGroup,alStatsNat=mibBuilder.importSymbols('ALTIGA-MIB','alNatGroup','alStatsNat')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaNatStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,28,2))
if mibBuilder.loadTexts:altigaNatStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaNatStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaNatStatsMibConformance=_AltigaNatStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,28,2,1))
_AltigaNatStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaNatStatsMibCompliances=_AltigaNatStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,28,2,1,1))
_AlStatsNatGlobal_ObjectIdentity=ObjectIdentity
alStatsNatGlobal=_AlStatsNatGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,23,1))
_AlNatStatsPacketsIn_Type=Counter32
_AlNatStatsPacketsIn_Object=MibScalar
alNatStatsPacketsIn=_AlNatStatsPacketsIn_Object((1,3,6,1,4,1,3076,2,1,2,23,1,1),_AlNatStatsPacketsIn_Type())
alNatStatsPacketsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatStatsPacketsIn.setStatus(_B)
_AlNatStatsPacketsOut_Type=Counter32
_AlNatStatsPacketsOut_Object=MibScalar
alNatStatsPacketsOut=_AlNatStatsPacketsOut_Object((1,3,6,1,4,1,3076,2,1,2,23,1,2),_AlNatStatsPacketsOut_Type())
alNatStatsPacketsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatStatsPacketsOut.setStatus(_B)
_AlNatStatsTotalTranslations_Type=Counter32
_AlNatStatsTotalTranslations_Object=MibScalar
alNatStatsTotalTranslations=_AlNatStatsTotalTranslations_Object((1,3,6,1,4,1,3076,2,1,2,23,1,3),_AlNatStatsTotalTranslations_Type())
alNatStatsTotalTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatStatsTotalTranslations.setStatus(_B)
_AlNatStatsActiveTranslations_Type=Counter32
_AlNatStatsActiveTranslations_Object=MibScalar
alNatStatsActiveTranslations=_AlNatStatsActiveTranslations_Object((1,3,6,1,4,1,3076,2,1,2,23,1,4),_AlNatStatsActiveTranslations_Type())
alNatStatsActiveTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatStatsActiveTranslations.setStatus(_B)
_AlNatStatsMaxTranslations_Type=Counter32
_AlNatStatsMaxTranslations_Object=MibScalar
alNatStatsMaxTranslations=_AlNatStatsMaxTranslations_Object((1,3,6,1,4,1,3076,2,1,2,23,1,5),_AlNatStatsMaxTranslations_Type())
alNatStatsMaxTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatStatsMaxTranslations.setStatus(_B)
_AlNatTranslationTable_Object=MibTable
alNatTranslationTable=_AlNatTranslationTable_Object((1,3,6,1,4,1,3076,2,1,2,23,2))
if mibBuilder.loadTexts:alNatTranslationTable.setStatus(_B)
_AlNatTranslationEntry_Object=MibTableRow
alNatTranslationEntry=_AlNatTranslationEntry_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1))
alNatTranslationEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:alNatTranslationEntry.setStatus(_B)
_AlNatTranslationSrcAddress_Type=IpAddress
_AlNatTranslationSrcAddress_Object=MibTableColumn
alNatTranslationSrcAddress=_AlNatTranslationSrcAddress_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,1),_AlNatTranslationSrcAddress_Type())
alNatTranslationSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationSrcAddress.setStatus(_B)
class _AlNatTranslationSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlNatTranslationSrcPort_Type.__name__=_D
_AlNatTranslationSrcPort_Object=MibTableColumn
alNatTranslationSrcPort=_AlNatTranslationSrcPort_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,2),_AlNatTranslationSrcPort_Type())
alNatTranslationSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationSrcPort.setStatus(_B)
_AlNatTranslationDestAddress_Type=IpAddress
_AlNatTranslationDestAddress_Object=MibTableColumn
alNatTranslationDestAddress=_AlNatTranslationDestAddress_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,3),_AlNatTranslationDestAddress_Type())
alNatTranslationDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationDestAddress.setStatus(_B)
class _AlNatTranslationDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlNatTranslationDestPort_Type.__name__=_D
_AlNatTranslationDestPort_Object=MibTableColumn
alNatTranslationDestPort=_AlNatTranslationDestPort_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,4),_AlNatTranslationDestPort_Type())
alNatTranslationDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationDestPort.setStatus(_B)
_AlNatTranslationAddress_Type=IpAddress
_AlNatTranslationAddress_Object=MibTableColumn
alNatTranslationAddress=_AlNatTranslationAddress_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,5),_AlNatTranslationAddress_Type())
alNatTranslationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationAddress.setStatus(_B)
class _AlNatTranslationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlNatTranslationPort_Type.__name__=_D
_AlNatTranslationPort_Object=MibTableColumn
alNatTranslationPort=_AlNatTranslationPort_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,6),_AlNatTranslationPort_Type())
alNatTranslationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationPort.setStatus(_B)
_AlNatTranslationAge_Type=Unsigned32
_AlNatTranslationAge_Object=MibTableColumn
alNatTranslationAge=_AlNatTranslationAge_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,7),_AlNatTranslationAge_Type())
alNatTranslationAge.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationAge.setStatus(_B)
class _AlNatTranslationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,8,16,32,64,128,256,512,1024,2048,4095)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,8),(_T,16),(_U,32),(_V,64),(_W,128),(_X,256),(_Y,512),(_Z,1024),(_a,2048),('all',4095)))
_AlNatTranslationType_Type.__name__=_D
_AlNatTranslationType_Object=MibTableColumn
alNatTranslationType=_AlNatTranslationType_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,8),_AlNatTranslationType_Type())
alNatTranslationType.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationType.setStatus(_B)
class _AlNatTranslationDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_AlNatTranslationDirection_Type.__name__=_D
_AlNatTranslationDirection_Object=MibTableColumn
alNatTranslationDirection=_AlNatTranslationDirection_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,9),_AlNatTranslationDirection_Type())
alNatTranslationDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationDirection.setStatus(_B)
_AlNatTranslationBytes_Type=Counter32
_AlNatTranslationBytes_Object=MibTableColumn
alNatTranslationBytes=_AlNatTranslationBytes_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,10),_AlNatTranslationBytes_Type())
alNatTranslationBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationBytes.setStatus(_B)
_AlNatTranslationPackets_Type=Counter32
_AlNatTranslationPackets_Object=MibTableColumn
alNatTranslationPackets=_AlNatTranslationPackets_Object((1,3,6,1,4,1,3076,2,1,2,23,2,1,11),_AlNatTranslationPackets_Type())
alNatTranslationPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatTranslationPackets.setStatus(_B)
_AlNatAllTranslationTable_Object=MibTable
alNatAllTranslationTable=_AlNatAllTranslationTable_Object((1,3,6,1,4,1,3076,2,1,2,23,3))
if mibBuilder.loadTexts:alNatAllTranslationTable.setStatus(_B)
_AlNatAllTranslationEntry_Object=MibTableRow
alNatAllTranslationEntry=_AlNatAllTranslationEntry_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1))
alNatAllTranslationEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:alNatAllTranslationEntry.setStatus(_B)
_AlNatAllTranslationSrcAddress_Type=IpAddress
_AlNatAllTranslationSrcAddress_Object=MibTableColumn
alNatAllTranslationSrcAddress=_AlNatAllTranslationSrcAddress_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,1),_AlNatAllTranslationSrcAddress_Type())
alNatAllTranslationSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationSrcAddress.setStatus(_B)
class _AlNatAllTranslationSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlNatAllTranslationSrcPort_Type.__name__=_D
_AlNatAllTranslationSrcPort_Object=MibTableColumn
alNatAllTranslationSrcPort=_AlNatAllTranslationSrcPort_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,2),_AlNatAllTranslationSrcPort_Type())
alNatAllTranslationSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationSrcPort.setStatus(_B)
_AlNatAllTranslationDestAddress_Type=IpAddress
_AlNatAllTranslationDestAddress_Object=MibTableColumn
alNatAllTranslationDestAddress=_AlNatAllTranslationDestAddress_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,3),_AlNatAllTranslationDestAddress_Type())
alNatAllTranslationDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationDestAddress.setStatus(_B)
class _AlNatAllTranslationDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlNatAllTranslationDestPort_Type.__name__=_D
_AlNatAllTranslationDestPort_Object=MibTableColumn
alNatAllTranslationDestPort=_AlNatAllTranslationDestPort_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,4),_AlNatAllTranslationDestPort_Type())
alNatAllTranslationDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationDestPort.setStatus(_B)
_AlNatAllTranslationAddress_Type=IpAddress
_AlNatAllTranslationAddress_Object=MibTableColumn
alNatAllTranslationAddress=_AlNatAllTranslationAddress_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,5),_AlNatAllTranslationAddress_Type())
alNatAllTranslationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationAddress.setStatus(_B)
class _AlNatAllTranslationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlNatAllTranslationPort_Type.__name__=_D
_AlNatAllTranslationPort_Object=MibTableColumn
alNatAllTranslationPort=_AlNatAllTranslationPort_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,6),_AlNatAllTranslationPort_Type())
alNatAllTranslationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationPort.setStatus(_B)
_AlNatAllTranslationAge_Type=Unsigned32
_AlNatAllTranslationAge_Object=MibTableColumn
alNatAllTranslationAge=_AlNatAllTranslationAge_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,7),_AlNatAllTranslationAge_Type())
alNatAllTranslationAge.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationAge.setStatus(_B)
class _AlNatAllTranslationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,8,16,32,64,128,256,512,1024,2048,4095)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,8),(_T,16),(_U,32),(_V,64),(_W,128),(_X,256),(_Y,512),(_Z,1024),(_a,2048),('all',4095)))
_AlNatAllTranslationType_Type.__name__=_D
_AlNatAllTranslationType_Object=MibTableColumn
alNatAllTranslationType=_AlNatAllTranslationType_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,8),_AlNatAllTranslationType_Type())
alNatAllTranslationType.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationType.setStatus(_B)
class _AlNatAllTranslationDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_AlNatAllTranslationDirection_Type.__name__=_D
_AlNatAllTranslationDirection_Object=MibTableColumn
alNatAllTranslationDirection=_AlNatAllTranslationDirection_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,9),_AlNatAllTranslationDirection_Type())
alNatAllTranslationDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationDirection.setStatus(_B)
_AlNatAllTranslationBytes_Type=Counter32
_AlNatAllTranslationBytes_Object=MibTableColumn
alNatAllTranslationBytes=_AlNatAllTranslationBytes_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,10),_AlNatAllTranslationBytes_Type())
alNatAllTranslationBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationBytes.setStatus(_B)
_AlNatAllTranslationPackets_Type=Counter32
_AlNatAllTranslationPackets_Object=MibTableColumn
alNatAllTranslationPackets=_AlNatAllTranslationPackets_Object((1,3,6,1,4,1,3076,2,1,2,23,3,1,11),_AlNatAllTranslationPackets_Type())
alNatAllTranslationPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alNatAllTranslationPackets.setStatus(_B)
altigaNatStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,23,2))
altigaNatStatsGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_p),(_A,_q),(_A,_r),(_A,_M),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:altigaNatStatsGroup.setStatus(_B)
altigaNatStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,28,2,1,1,1))
altigaNatStatsMibCompliance.setObjects((_A,_v))
if mibBuilder.loadTexts:altigaNatStatsMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'altigaNatStatsMibModule':altigaNatStatsMibModule,'altigaNatStatsMibConformance':altigaNatStatsMibConformance,'altigaNatStatsMibCompliances':altigaNatStatsMibCompliances,'altigaNatStatsMibCompliance':altigaNatStatsMibCompliance,_v:altigaNatStatsGroup,'alStatsNatGlobal':alStatsNatGlobal,_d:alNatStatsPacketsIn,_e:alNatStatsPacketsOut,_f:alNatStatsTotalTranslations,_g:alNatStatsActiveTranslations,_h:alNatStatsMaxTranslations,'alNatTranslationTable':alNatTranslationTable,'alNatTranslationEntry':alNatTranslationEntry,_E:alNatTranslationSrcAddress,_F:alNatTranslationSrcPort,_G:alNatTranslationDestAddress,_H:alNatTranslationDestPort,_i:alNatTranslationAddress,_j:alNatTranslationPort,_k:alNatTranslationAge,_l:alNatTranslationType,_m:alNatTranslationDirection,_n:alNatTranslationBytes,_o:alNatTranslationPackets,'alNatAllTranslationTable':alNatAllTranslationTable,'alNatAllTranslationEntry':alNatAllTranslationEntry,_I:alNatAllTranslationSrcAddress,_J:alNatAllTranslationSrcPort,_K:alNatAllTranslationDestAddress,_L:alNatAllTranslationDestPort,_p:alNatAllTranslationAddress,_q:alNatAllTranslationPort,_r:alNatAllTranslationAge,_M:alNatAllTranslationType,_s:alNatAllTranslationDirection,_t:alNatAllTranslationBytes,_u:alNatAllTranslationPackets})