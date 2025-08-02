_K='altigaSslStatsGroup'
_J='alSslStatsPostEncryptOctets'
_I='alSslStatsPreEncryptOctets'
_H='alSslStatsPostDecryptOctets'
_G='alSslStatsPreDecryptOctets'
_F='alSslStatsMaxSessions'
_E='alSslStatsActiveSessions'
_D='alSslStatsTotalSessions'
_C='read-only'
_B='ALTIGA-SSL-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alSslMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alSslMibModule')
alSslGroup,alStatsSsl=mibBuilder.importSymbols('ALTIGA-MIB','alSslGroup','alStatsSsl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaSslStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,31,2))
if mibBuilder.loadTexts:altigaSslStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaSslStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaSslStatsMibConformance=_AltigaSslStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,31,2,1))
_AltigaSslStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaSslStatsMibCompliances=_AltigaSslStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,31,2,1,1))
_AlStatsSslGlobal_ObjectIdentity=ObjectIdentity
alStatsSslGlobal=_AlStatsSslGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,26,1))
_AlSslStatsTotalSessions_Type=Counter32
_AlSslStatsTotalSessions_Object=MibScalar
alSslStatsTotalSessions=_AlSslStatsTotalSessions_Object((1,3,6,1,4,1,3076,2,1,2,26,1,1),_AlSslStatsTotalSessions_Type())
alSslStatsTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alSslStatsTotalSessions.setStatus(_A)
_AlSslStatsActiveSessions_Type=Gauge32
_AlSslStatsActiveSessions_Object=MibScalar
alSslStatsActiveSessions=_AlSslStatsActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,26,1,2),_AlSslStatsActiveSessions_Type())
alSslStatsActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alSslStatsActiveSessions.setStatus(_A)
_AlSslStatsMaxSessions_Type=Gauge32
_AlSslStatsMaxSessions_Object=MibScalar
alSslStatsMaxSessions=_AlSslStatsMaxSessions_Object((1,3,6,1,4,1,3076,2,1,2,26,1,3),_AlSslStatsMaxSessions_Type())
alSslStatsMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alSslStatsMaxSessions.setStatus(_A)
_AlSslStatsPreDecryptOctets_Type=Counter32
_AlSslStatsPreDecryptOctets_Object=MibScalar
alSslStatsPreDecryptOctets=_AlSslStatsPreDecryptOctets_Object((1,3,6,1,4,1,3076,2,1,2,26,1,4),_AlSslStatsPreDecryptOctets_Type())
alSslStatsPreDecryptOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alSslStatsPreDecryptOctets.setStatus(_A)
_AlSslStatsPostDecryptOctets_Type=Counter32
_AlSslStatsPostDecryptOctets_Object=MibScalar
alSslStatsPostDecryptOctets=_AlSslStatsPostDecryptOctets_Object((1,3,6,1,4,1,3076,2,1,2,26,1,5),_AlSslStatsPostDecryptOctets_Type())
alSslStatsPostDecryptOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alSslStatsPostDecryptOctets.setStatus(_A)
_AlSslStatsPreEncryptOctets_Type=Counter32
_AlSslStatsPreEncryptOctets_Object=MibScalar
alSslStatsPreEncryptOctets=_AlSslStatsPreEncryptOctets_Object((1,3,6,1,4,1,3076,2,1,2,26,1,6),_AlSslStatsPreEncryptOctets_Type())
alSslStatsPreEncryptOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alSslStatsPreEncryptOctets.setStatus(_A)
_AlSslStatsPostEncryptOctets_Type=Counter32
_AlSslStatsPostEncryptOctets_Object=MibScalar
alSslStatsPostEncryptOctets=_AlSslStatsPostEncryptOctets_Object((1,3,6,1,4,1,3076,2,1,2,26,1,7),_AlSslStatsPostEncryptOctets_Type())
alSslStatsPostEncryptOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alSslStatsPostEncryptOctets.setStatus(_A)
altigaSslStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,26,2))
altigaSslStatsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:altigaSslStatsGroup.setStatus(_A)
altigaSslStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,31,2,1,1,1))
altigaSslStatsMibCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:altigaSslStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaSslStatsMibModule':altigaSslStatsMibModule,'altigaSslStatsMibConformance':altigaSslStatsMibConformance,'altigaSslStatsMibCompliances':altigaSslStatsMibCompliances,'altigaSslStatsMibCompliance':altigaSslStatsMibCompliance,_K:altigaSslStatsGroup,'alStatsSslGlobal':alStatsSslGlobal,_D:alSslStatsTotalSessions,_E:alSslStatsActiveSessions,_F:alSslStatsMaxSessions,_G:alSslStatsPreDecryptOctets,_H:alSslStatsPostDecryptOctets,_I:alSslStatsPreEncryptOctets,_J:alSslStatsPostEncryptOctets})