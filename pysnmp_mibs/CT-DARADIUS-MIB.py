_M='ssIndex'
_L='secondaryAccounting'
_K='primaryAccounting'
_J='secondaryAuthentication'
_I='primaryAuthentication'
_H='scIndex'
_G='disabled'
_F='enabled'
_E='CT-DARADIUS-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtSSA_ObjectIdentity=ObjectIdentity
ctSSA=_CtSSA_ObjectIdentity((1,3,6,1,4,1,52,4497))
_DaRadius_ObjectIdentity=ObjectIdentity
daRadius=_DaRadius_ObjectIdentity((1,3,6,1,4,1,52,4497,24))
_DaRadiusConfig_ObjectIdentity=ObjectIdentity
daRadiusConfig=_DaRadiusConfig_ObjectIdentity((1,3,6,1,4,1,52,4497,24,1))
_DaRadiusGeneralConfig_ObjectIdentity=ObjectIdentity
daRadiusGeneralConfig=_DaRadiusGeneralConfig_ObjectIdentity((1,3,6,1,4,1,52,4497,24,1,1))
class _DaRadiusgcEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DaRadiusgcEnabled_Type.__name__=_D
_DaRadiusgcEnabled_Object=MibScalar
daRadiusgcEnabled=_DaRadiusgcEnabled_Object((1,3,6,1,4,1,52,4497,24,1,1,1),_DaRadiusgcEnabled_Type())
daRadiusgcEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:daRadiusgcEnabled.setStatus(_A)
_DaRadiusgcAuthNumRetries_Type=Integer32
_DaRadiusgcAuthNumRetries_Object=MibScalar
daRadiusgcAuthNumRetries=_DaRadiusgcAuthNumRetries_Object((1,3,6,1,4,1,52,4497,24,1,1,2),_DaRadiusgcAuthNumRetries_Type())
daRadiusgcAuthNumRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:daRadiusgcAuthNumRetries.setStatus(_A)
_DaRadiusgcAuthSecsBtwnRetries_Type=Integer32
_DaRadiusgcAuthSecsBtwnRetries_Object=MibScalar
daRadiusgcAuthSecsBtwnRetries=_DaRadiusgcAuthSecsBtwnRetries_Object((1,3,6,1,4,1,52,4497,24,1,1,3),_DaRadiusgcAuthSecsBtwnRetries_Type())
daRadiusgcAuthSecsBtwnRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:daRadiusgcAuthSecsBtwnRetries.setStatus(_A)
_DaRadiusgcAcctNumRetries_Type=Integer32
_DaRadiusgcAcctNumRetries_Object=MibScalar
daRadiusgcAcctNumRetries=_DaRadiusgcAcctNumRetries_Object((1,3,6,1,4,1,52,4497,24,1,1,4),_DaRadiusgcAcctNumRetries_Type())
daRadiusgcAcctNumRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:daRadiusgcAcctNumRetries.setStatus(_A)
_GcAcctSecsBtwnRetries_Type=Integer32
_GcAcctSecsBtwnRetries_Object=MibScalar
gcAcctSecsBtwnRetries=_GcAcctSecsBtwnRetries_Object((1,3,6,1,4,1,52,4497,24,1,1,5),_GcAcctSecsBtwnRetries_Type())
gcAcctSecsBtwnRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:gcAcctSecsBtwnRetries.setStatus(_A)
_DaRadiusServerCfgTable_Object=MibTable
daRadiusServerCfgTable=_DaRadiusServerCfgTable_Object((1,3,6,1,4,1,52,4497,24,1,2))
if mibBuilder.loadTexts:daRadiusServerCfgTable.setStatus(_A)
_DaRadiusServerCfgEntry_Object=MibTableRow
daRadiusServerCfgEntry=_DaRadiusServerCfgEntry_Object((1,3,6,1,4,1,52,4497,24,1,2,1))
daRadiusServerCfgEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:daRadiusServerCfgEntry.setStatus(_A)
class _ScIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_ScIndex_Type.__name__=_D
_ScIndex_Object=MibTableColumn
scIndex=_ScIndex_Object((1,3,6,1,4,1,52,4497,24,1,2,1,1),_ScIndex_Type())
scIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scIndex.setStatus(_A)
class _ScStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ScStatus_Type.__name__=_D
_ScStatus_Object=MibTableColumn
scStatus=_ScStatus_Object((1,3,6,1,4,1,52,4497,24,1,2,1,2),_ScStatus_Type())
scStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:scStatus.setStatus(_A)
_ScIpAddress_Type=IpAddress
_ScIpAddress_Object=MibTableColumn
scIpAddress=_ScIpAddress_Object((1,3,6,1,4,1,52,4497,24,1,2,1,3),_ScIpAddress_Type())
scIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:scIpAddress.setStatus(_A)
_ScSharedSecret_Type=DisplayString
_ScSharedSecret_Object=MibTableColumn
scSharedSecret=_ScSharedSecret_Object((1,3,6,1,4,1,52,4497,24,1,2,1,4),_ScSharedSecret_Type())
scSharedSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:scSharedSecret.setStatus(_A)
_ScUdpPort_Type=Integer32
_ScUdpPort_Object=MibTableColumn
scUdpPort=_ScUdpPort_Object((1,3,6,1,4,1,52,4497,24,1,2,1,5),_ScUdpPort_Type())
scUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:scUdpPort.setStatus(_A)
_DaRadiusStats_ObjectIdentity=ObjectIdentity
daRadiusStats=_DaRadiusStats_ObjectIdentity((1,3,6,1,4,1,52,4497,24,2))
_DaRadiusGeneralStats_ObjectIdentity=ObjectIdentity
daRadiusGeneralStats=_DaRadiusGeneralStats_ObjectIdentity((1,3,6,1,4,1,52,4497,24,2,1))
_GsInDiscards_Type=Integer32
_GsInDiscards_Object=MibScalar
gsInDiscards=_GsInDiscards_Object((1,3,6,1,4,1,52,4497,24,2,1,1),_GsInDiscards_Type())
gsInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:gsInDiscards.setStatus(_A)
_GsInErrors_Type=Integer32
_GsInErrors_Object=MibScalar
gsInErrors=_GsInErrors_Object((1,3,6,1,4,1,52,4497,24,2,1,2),_GsInErrors_Type())
gsInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:gsInErrors.setStatus(_A)
_DaRadiusServerStatsTable_Object=MibTable
daRadiusServerStatsTable=_DaRadiusServerStatsTable_Object((1,3,6,1,4,1,52,4497,24,2,2))
if mibBuilder.loadTexts:daRadiusServerStatsTable.setStatus(_A)
_DaRadiusServerStatsEntry_Object=MibTableRow
daRadiusServerStatsEntry=_DaRadiusServerStatsEntry_Object((1,3,6,1,4,1,52,4497,24,2,2,1))
daRadiusServerStatsEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:daRadiusServerStatsEntry.setStatus(_A)
class _SsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_SsIndex_Type.__name__=_D
_SsIndex_Object=MibTableColumn
ssIndex=_SsIndex_Object((1,3,6,1,4,1,52,4497,24,2,2,1,1),_SsIndex_Type())
ssIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ssIndex.setStatus(_A)
_SsInPkts_Type=Integer32
_SsInPkts_Object=MibTableColumn
ssInPkts=_SsInPkts_Object((1,3,6,1,4,1,52,4497,24,2,2,1,2),_SsInPkts_Type())
ssInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ssInPkts.setStatus(_A)
_SsInDiscards_Type=Integer32
_SsInDiscards_Object=MibTableColumn
ssInDiscards=_SsInDiscards_Object((1,3,6,1,4,1,52,4497,24,2,2,1,3),_SsInDiscards_Type())
ssInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ssInDiscards.setStatus(_A)
_SsInErrors_Type=Integer32
_SsInErrors_Object=MibTableColumn
ssInErrors=_SsInErrors_Object((1,3,6,1,4,1,52,4497,24,2,2,1,4),_SsInErrors_Type())
ssInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ssInErrors.setStatus(_A)
_SsOutPkts_Type=Integer32
_SsOutPkts_Object=MibTableColumn
ssOutPkts=_SsOutPkts_Object((1,3,6,1,4,1,52,4497,24,2,2,1,5),_SsOutPkts_Type())
ssOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ssOutPkts.setStatus(_A)
_SsOutErrors_Type=Integer32
_SsOutErrors_Object=MibTableColumn
ssOutErrors=_SsOutErrors_Object((1,3,6,1,4,1,52,4497,24,2,2,1,6),_SsOutErrors_Type())
ssOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ssOutErrors.setStatus(_A)
_SsResponseTimeouts_Type=Integer32
_SsResponseTimeouts_Object=MibTableColumn
ssResponseTimeouts=_SsResponseTimeouts_Object((1,3,6,1,4,1,52,4497,24,2,2,1,7),_SsResponseTimeouts_Type())
ssResponseTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:ssResponseTimeouts.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ctSSA':ctSSA,'daRadius':daRadius,'daRadiusConfig':daRadiusConfig,'daRadiusGeneralConfig':daRadiusGeneralConfig,'daRadiusgcEnabled':daRadiusgcEnabled,'daRadiusgcAuthNumRetries':daRadiusgcAuthNumRetries,'daRadiusgcAuthSecsBtwnRetries':daRadiusgcAuthSecsBtwnRetries,'daRadiusgcAcctNumRetries':daRadiusgcAcctNumRetries,'gcAcctSecsBtwnRetries':gcAcctSecsBtwnRetries,'daRadiusServerCfgTable':daRadiusServerCfgTable,'daRadiusServerCfgEntry':daRadiusServerCfgEntry,_H:scIndex,'scStatus':scStatus,'scIpAddress':scIpAddress,'scSharedSecret':scSharedSecret,'scUdpPort':scUdpPort,'daRadiusStats':daRadiusStats,'daRadiusGeneralStats':daRadiusGeneralStats,'gsInDiscards':gsInDiscards,'gsInErrors':gsInErrors,'daRadiusServerStatsTable':daRadiusServerStatsTable,'daRadiusServerStatsEntry':daRadiusServerStatsEntry,_M:ssIndex,'ssInPkts':ssInPkts,'ssInDiscards':ssInDiscards,'ssInErrors':ssInErrors,'ssOutPkts':ssOutPkts,'ssOutErrors':ssOutErrors,'ssResponseTimeouts':ssResponseTimeouts})