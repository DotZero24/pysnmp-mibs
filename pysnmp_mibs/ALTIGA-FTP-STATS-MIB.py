_Q='altigaFtpStatsGroup'
_P='alFtpClientStatsTimeouts'
_O='alFtpClientStatsOctetsRecv'
_N='alFtpClientStatsOctetsXmit'
_M='alFtpClientStatsBinaryXfers'
_L='alFtpClientStatsAsciiXfers'
_K='alFtpClientStatsBadFileXfers'
_J='alFtpClientStatsGoodFileXfers'
_I='alFtpClientStatsBadDataConns'
_H='alFtpClientStatsGoodDataConns'
_G='alFtpClientStatsBadConns'
_F='alFtpClientStatsGoodConns'
_E='alFtpClientStatsTotalSess'
_D='alFtpClientStatsMaxSess'
_C='read-only'
_B='ALTIGA-FTP-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alFtpMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alFtpMibModule')
alFtpGroup,alStatsFtp=mibBuilder.importSymbols('ALTIGA-MIB','alFtpGroup','alStatsFtp')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaFtpStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,17,2))
if mibBuilder.loadTexts:altigaFtpStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaFtpStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaFtpStatsMibConformance=_AltigaFtpStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,17,2,1))
_AltigaFtpStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaFtpStatsMibCompliances=_AltigaFtpStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,17,2,1,1))
_AlStatsFtpServerGlobal_ObjectIdentity=ObjectIdentity
alStatsFtpServerGlobal=_AlStatsFtpServerGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,12,1))
_AlStatsFtpClientGlobal_ObjectIdentity=ObjectIdentity
alStatsFtpClientGlobal=_AlStatsFtpClientGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,12,2))
_AlFtpClientStatsMaxSess_Type=Gauge32
_AlFtpClientStatsMaxSess_Object=MibScalar
alFtpClientStatsMaxSess=_AlFtpClientStatsMaxSess_Object((1,3,6,1,4,1,3076,2,1,2,12,2,1),_AlFtpClientStatsMaxSess_Type())
alFtpClientStatsMaxSess.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsMaxSess.setStatus(_A)
_AlFtpClientStatsTotalSess_Type=Counter32
_AlFtpClientStatsTotalSess_Object=MibScalar
alFtpClientStatsTotalSess=_AlFtpClientStatsTotalSess_Object((1,3,6,1,4,1,3076,2,1,2,12,2,2),_AlFtpClientStatsTotalSess_Type())
alFtpClientStatsTotalSess.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsTotalSess.setStatus(_A)
_AlFtpClientStatsGoodConns_Type=Counter32
_AlFtpClientStatsGoodConns_Object=MibScalar
alFtpClientStatsGoodConns=_AlFtpClientStatsGoodConns_Object((1,3,6,1,4,1,3076,2,1,2,12,2,3),_AlFtpClientStatsGoodConns_Type())
alFtpClientStatsGoodConns.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsGoodConns.setStatus(_A)
_AlFtpClientStatsBadConns_Type=Counter32
_AlFtpClientStatsBadConns_Object=MibScalar
alFtpClientStatsBadConns=_AlFtpClientStatsBadConns_Object((1,3,6,1,4,1,3076,2,1,2,12,2,4),_AlFtpClientStatsBadConns_Type())
alFtpClientStatsBadConns.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsBadConns.setStatus(_A)
_AlFtpClientStatsGoodDataConns_Type=Counter32
_AlFtpClientStatsGoodDataConns_Object=MibScalar
alFtpClientStatsGoodDataConns=_AlFtpClientStatsGoodDataConns_Object((1,3,6,1,4,1,3076,2,1,2,12,2,5),_AlFtpClientStatsGoodDataConns_Type())
alFtpClientStatsGoodDataConns.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsGoodDataConns.setStatus(_A)
_AlFtpClientStatsBadDataConns_Type=Counter32
_AlFtpClientStatsBadDataConns_Object=MibScalar
alFtpClientStatsBadDataConns=_AlFtpClientStatsBadDataConns_Object((1,3,6,1,4,1,3076,2,1,2,12,2,6),_AlFtpClientStatsBadDataConns_Type())
alFtpClientStatsBadDataConns.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsBadDataConns.setStatus(_A)
_AlFtpClientStatsGoodFileXfers_Type=Counter32
_AlFtpClientStatsGoodFileXfers_Object=MibScalar
alFtpClientStatsGoodFileXfers=_AlFtpClientStatsGoodFileXfers_Object((1,3,6,1,4,1,3076,2,1,2,12,2,7),_AlFtpClientStatsGoodFileXfers_Type())
alFtpClientStatsGoodFileXfers.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsGoodFileXfers.setStatus(_A)
_AlFtpClientStatsBadFileXfers_Type=Counter32
_AlFtpClientStatsBadFileXfers_Object=MibScalar
alFtpClientStatsBadFileXfers=_AlFtpClientStatsBadFileXfers_Object((1,3,6,1,4,1,3076,2,1,2,12,2,8),_AlFtpClientStatsBadFileXfers_Type())
alFtpClientStatsBadFileXfers.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsBadFileXfers.setStatus(_A)
_AlFtpClientStatsAsciiXfers_Type=Counter32
_AlFtpClientStatsAsciiXfers_Object=MibScalar
alFtpClientStatsAsciiXfers=_AlFtpClientStatsAsciiXfers_Object((1,3,6,1,4,1,3076,2,1,2,12,2,9),_AlFtpClientStatsAsciiXfers_Type())
alFtpClientStatsAsciiXfers.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsAsciiXfers.setStatus(_A)
_AlFtpClientStatsBinaryXfers_Type=Counter32
_AlFtpClientStatsBinaryXfers_Object=MibScalar
alFtpClientStatsBinaryXfers=_AlFtpClientStatsBinaryXfers_Object((1,3,6,1,4,1,3076,2,1,2,12,2,10),_AlFtpClientStatsBinaryXfers_Type())
alFtpClientStatsBinaryXfers.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsBinaryXfers.setStatus(_A)
_AlFtpClientStatsOctetsXmit_Type=Counter32
_AlFtpClientStatsOctetsXmit_Object=MibScalar
alFtpClientStatsOctetsXmit=_AlFtpClientStatsOctetsXmit_Object((1,3,6,1,4,1,3076,2,1,2,12,2,11),_AlFtpClientStatsOctetsXmit_Type())
alFtpClientStatsOctetsXmit.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsOctetsXmit.setStatus(_A)
_AlFtpClientStatsOctetsRecv_Type=Counter32
_AlFtpClientStatsOctetsRecv_Object=MibScalar
alFtpClientStatsOctetsRecv=_AlFtpClientStatsOctetsRecv_Object((1,3,6,1,4,1,3076,2,1,2,12,2,12),_AlFtpClientStatsOctetsRecv_Type())
alFtpClientStatsOctetsRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsOctetsRecv.setStatus(_A)
_AlFtpClientStatsTimeouts_Type=Counter32
_AlFtpClientStatsTimeouts_Object=MibScalar
alFtpClientStatsTimeouts=_AlFtpClientStatsTimeouts_Object((1,3,6,1,4,1,3076,2,1,2,12,2,13),_AlFtpClientStatsTimeouts_Type())
alFtpClientStatsTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:alFtpClientStatsTimeouts.setStatus(_A)
altigaFtpStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,12,2))
altigaFtpStatsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:altigaFtpStatsGroup.setStatus(_A)
altigaFtpStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,17,2,1,1,1))
altigaFtpStatsMibCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:altigaFtpStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaFtpStatsMibModule':altigaFtpStatsMibModule,'altigaFtpStatsMibConformance':altigaFtpStatsMibConformance,'altigaFtpStatsMibCompliances':altigaFtpStatsMibCompliances,'altigaFtpStatsMibCompliance':altigaFtpStatsMibCompliance,_Q:altigaFtpStatsGroup,'alStatsFtpServerGlobal':alStatsFtpServerGlobal,'alStatsFtpClientGlobal':alStatsFtpClientGlobal,_D:alFtpClientStatsMaxSess,_E:alFtpClientStatsTotalSess,_F:alFtpClientStatsGoodConns,_G:alFtpClientStatsBadConns,_H:alFtpClientStatsGoodDataConns,_I:alFtpClientStatsBadDataConns,_J:alFtpClientStatsGoodFileXfers,_K:alFtpClientStatsBadFileXfers,_L:alFtpClientStatsAsciiXfers,_M:alFtpClientStatsBinaryXfers,_N:alFtpClientStatsOctetsXmit,_O:alFtpClientStatsOctetsRecv,_P:alFtpClientStatsTimeouts})