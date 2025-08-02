_I='ruckusHLRIndex'
_H='ruckusGGSNGTPCIndex'
_G='ruckusGTPUIndex'
_F='ruckusCGFIndex'
_E='ruckusAAAProxyIndex'
_D='ruckusAAAIndex'
_C='RUCKUS-SCG-TTG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusSCGTTGModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusSCGTTGModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ruckusTTGMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,3,3,1))
_RuckusTTGObjects_ObjectIdentity=ObjectIdentity
ruckusTTGObjects=_RuckusTTGObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,3,3,1,1))
_RuckusAAAInfo_ObjectIdentity=ObjectIdentity
ruckusAAAInfo=_RuckusAAAInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,3,3,1,1,1))
_RuckusAAATable_Object=MibTable
ruckusAAATable=_RuckusAAATable_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1))
if mibBuilder.loadTexts:ruckusAAATable.setStatus(_A)
_RuckusAAAEntry_Object=MibTableRow
ruckusAAAEntry=_RuckusAAAEntry_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1))
ruckusAAAEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ruckusAAAEntry.setStatus(_A)
_RuckusAAAAaaIp_Type=DisplayString
_RuckusAAAAaaIp_Object=MibTableColumn
ruckusAAAAaaIp=_RuckusAAAAaaIp_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,1),_RuckusAAAAaaIp_Type())
ruckusAAAAaaIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAAaaIp.setStatus(_A)
_RuckusAAANumSuccAuthPerm_Type=Counter64
_RuckusAAANumSuccAuthPerm_Object=MibTableColumn
ruckusAAANumSuccAuthPerm=_RuckusAAANumSuccAuthPerm_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,2),_RuckusAAANumSuccAuthPerm_Type())
ruckusAAANumSuccAuthPerm.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumSuccAuthPerm.setStatus(_A)
_RuckusAAANumFailAuthPerm_Type=Counter64
_RuckusAAANumFailAuthPerm_Object=MibTableColumn
ruckusAAANumFailAuthPerm=_RuckusAAANumFailAuthPerm_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,3),_RuckusAAANumFailAuthPerm_Type())
ruckusAAANumFailAuthPerm.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumFailAuthPerm.setStatus(_A)
_RuckusAAANumSuccAuthPsd_Type=Counter64
_RuckusAAANumSuccAuthPsd_Object=MibTableColumn
ruckusAAANumSuccAuthPsd=_RuckusAAANumSuccAuthPsd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,4),_RuckusAAANumSuccAuthPsd_Type())
ruckusAAANumSuccAuthPsd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumSuccAuthPsd.setStatus(_A)
_RuckusAAANumFailAuthPsd_Type=Counter64
_RuckusAAANumFailAuthPsd_Object=MibTableColumn
ruckusAAANumFailAuthPsd=_RuckusAAANumFailAuthPsd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,5),_RuckusAAANumFailAuthPsd_Type())
ruckusAAANumFailAuthPsd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumFailAuthPsd.setStatus(_A)
_RuckusAAANumSuccFastAuth_Type=Counter64
_RuckusAAANumSuccFastAuth_Object=MibTableColumn
ruckusAAANumSuccFastAuth=_RuckusAAANumSuccFastAuth_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,6),_RuckusAAANumSuccFastAuth_Type())
ruckusAAANumSuccFastAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumSuccFastAuth.setStatus(_A)
_RuckusAAANumFailFastAuth_Type=Counter64
_RuckusAAANumFailFastAuth_Object=MibTableColumn
ruckusAAANumFailFastAuth=_RuckusAAANumFailFastAuth_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,7),_RuckusAAANumFailFastAuth_Type())
ruckusAAANumFailFastAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumFailFastAuth.setStatus(_A)
_RuckusAAANumAuthUnknPsd_Type=Counter64
_RuckusAAANumAuthUnknPsd_Object=MibTableColumn
ruckusAAANumAuthUnknPsd=_RuckusAAANumAuthUnknPsd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,8),_RuckusAAANumAuthUnknPsd_Type())
ruckusAAANumAuthUnknPsd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumAuthUnknPsd.setStatus(_A)
_RuckusAAANumAuthUnknFR_Type=Counter64
_RuckusAAANumAuthUnknFR_Object=MibTableColumn
ruckusAAANumAuthUnknFR=_RuckusAAANumAuthUnknFR_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,9),_RuckusAAANumAuthUnknFR_Type())
ruckusAAANumAuthUnknFR.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumAuthUnknFR.setStatus(_A)
_RuckusAAANumIncompleteAuth_Type=Counter64
_RuckusAAANumIncompleteAuth_Object=MibTableColumn
ruckusAAANumIncompleteAuth=_RuckusAAANumIncompleteAuth_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,10),_RuckusAAANumIncompleteAuth_Type())
ruckusAAANumIncompleteAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumIncompleteAuth.setStatus(_A)
_RuckusAAANumSuccAcc_Type=Counter64
_RuckusAAANumSuccAcc_Object=MibTableColumn
ruckusAAANumSuccAcc=_RuckusAAANumSuccAcc_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,11),_RuckusAAANumSuccAcc_Type())
ruckusAAANumSuccAcc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumSuccAcc.setStatus(_A)
_RuckusAAANumFailAcc_Type=Counter64
_RuckusAAANumFailAcc_Object=MibTableColumn
ruckusAAANumFailAcc=_RuckusAAANumFailAcc_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,12),_RuckusAAANumFailAcc_Type())
ruckusAAANumFailAcc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumFailAcc.setStatus(_A)
_RuckusAAANumRadAcsRq_Type=Counter64
_RuckusAAANumRadAcsRq_Object=MibTableColumn
ruckusAAANumRadAcsRq=_RuckusAAANumRadAcsRq_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,13),_RuckusAAANumRadAcsRq_Type())
ruckusAAANumRadAcsRq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadAcsRq.setStatus(_A)
_RuckusAAANumRadAcsAcpt_Type=Counter64
_RuckusAAANumRadAcsAcpt_Object=MibTableColumn
ruckusAAANumRadAcsAcpt=_RuckusAAANumRadAcsAcpt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,14),_RuckusAAANumRadAcsAcpt_Type())
ruckusAAANumRadAcsAcpt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadAcsAcpt.setStatus(_A)
_RuckusAAANumRadAcsChlg_Type=Counter64
_RuckusAAANumRadAcsChlg_Object=MibTableColumn
ruckusAAANumRadAcsChlg=_RuckusAAANumRadAcsChlg_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,15),_RuckusAAANumRadAcsChlg_Type())
ruckusAAANumRadAcsChlg.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadAcsChlg.setStatus(_A)
_RuckusAAANumRadAcsRej_Type=Counter64
_RuckusAAANumRadAcsRej_Object=MibTableColumn
ruckusAAANumRadAcsRej=_RuckusAAANumRadAcsRej_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,16),_RuckusAAANumRadAcsRej_Type())
ruckusAAANumRadAcsRej.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadAcsRej.setStatus(_A)
_RuckusAAANumRadAccRq_Type=Counter64
_RuckusAAANumRadAccRq_Object=MibTableColumn
ruckusAAANumRadAccRq=_RuckusAAANumRadAccRq_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,17),_RuckusAAANumRadAccRq_Type())
ruckusAAANumRadAccRq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadAccRq.setStatus(_A)
_RuckusAAANumRadAccAcpt_Type=Counter64
_RuckusAAANumRadAccAcpt_Object=MibTableColumn
ruckusAAANumRadAccAcpt=_RuckusAAANumRadAccAcpt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,18),_RuckusAAANumRadAccAcpt_Type())
ruckusAAANumRadAccAcpt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadAccAcpt.setStatus(_A)
_RuckusAAANumRadCoaRq_Type=Counter64
_RuckusAAANumRadCoaRq_Object=MibTableColumn
ruckusAAANumRadCoaRq=_RuckusAAANumRadCoaRq_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,19),_RuckusAAANumRadCoaRq_Type())
ruckusAAANumRadCoaRq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadCoaRq.setStatus(_A)
_RuckusAAANumSuccCoaAcpt_Type=Counter64
_RuckusAAANumSuccCoaAcpt_Object=MibTableColumn
ruckusAAANumSuccCoaAcpt=_RuckusAAANumSuccCoaAcpt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,20),_RuckusAAANumSuccCoaAcpt_Type())
ruckusAAANumSuccCoaAcpt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumSuccCoaAcpt.setStatus(_A)
_RuckusAAANumFailCoaAcpt_Type=Counter64
_RuckusAAANumFailCoaAcpt_Object=MibTableColumn
ruckusAAANumFailCoaAcpt=_RuckusAAANumFailCoaAcpt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,21),_RuckusAAANumFailCoaAcpt_Type())
ruckusAAANumFailCoaAcpt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumFailCoaAcpt.setStatus(_A)
_RuckusAAANumRadDmRq_Type=Counter64
_RuckusAAANumRadDmRq_Object=MibTableColumn
ruckusAAANumRadDmRq=_RuckusAAANumRadDmRq_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,22),_RuckusAAANumRadDmRq_Type())
ruckusAAANumRadDmRq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumRadDmRq.setStatus(_A)
_RuckusAAANumSuccDmAcpt_Type=Counter64
_RuckusAAANumSuccDmAcpt_Object=MibTableColumn
ruckusAAANumSuccDmAcpt=_RuckusAAANumSuccDmAcpt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,23),_RuckusAAANumSuccDmAcpt_Type())
ruckusAAANumSuccDmAcpt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumSuccDmAcpt.setStatus(_A)
_RuckusAAANumFailDmAcpt_Type=Counter64
_RuckusAAANumFailDmAcpt_Object=MibTableColumn
ruckusAAANumFailDmAcpt=_RuckusAAANumFailDmAcpt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,24),_RuckusAAANumFailDmAcpt_Type())
ruckusAAANumFailDmAcpt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAANumFailDmAcpt.setStatus(_A)
_RuckusAAAIndex_Type=Integer32
_RuckusAAAIndex_Object=MibTableColumn
ruckusAAAIndex=_RuckusAAAIndex_Object((1,3,6,1,4,1,25053,1,3,3,1,1,1,1,1,99),_RuckusAAAIndex_Type())
ruckusAAAIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAIndex.setStatus(_A)
_RuckusAAAProxyInfo_ObjectIdentity=ObjectIdentity
ruckusAAAProxyInfo=_RuckusAAAProxyInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,3,3,1,1,2))
_RuckusAAAProxyTable_Object=MibTable
ruckusAAAProxyTable=_RuckusAAAProxyTable_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1))
if mibBuilder.loadTexts:ruckusAAAProxyTable.setStatus(_A)
_RuckusAAAProxyEntry_Object=MibTableRow
ruckusAAAProxyEntry=_RuckusAAAProxyEntry_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1))
ruckusAAAProxyEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:ruckusAAAProxyEntry.setStatus(_A)
_RuckusAAAProxyAaaIp_Type=DisplayString
_RuckusAAAProxyAaaIp_Object=MibTableColumn
ruckusAAAProxyAaaIp=_RuckusAAAProxyAaaIp_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,1),_RuckusAAAProxyAaaIp_Type())
ruckusAAAProxyAaaIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyAaaIp.setStatus(_A)
_RuckusAAAProxyNumSuccAuth_Type=Counter64
_RuckusAAAProxyNumSuccAuth_Object=MibTableColumn
ruckusAAAProxyNumSuccAuth=_RuckusAAAProxyNumSuccAuth_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,2),_RuckusAAAProxyNumSuccAuth_Type())
ruckusAAAProxyNumSuccAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumSuccAuth.setStatus(_A)
_RuckusAAAProxyNumFailAuth_Type=Counter64
_RuckusAAAProxyNumFailAuth_Object=MibTableColumn
ruckusAAAProxyNumFailAuth=_RuckusAAAProxyNumFailAuth_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,3),_RuckusAAAProxyNumFailAuth_Type())
ruckusAAAProxyNumFailAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumFailAuth.setStatus(_A)
_RuckusAAAProxyNumIncmpltAuth_Type=Counter64
_RuckusAAAProxyNumIncmpltAuth_Object=MibTableColumn
ruckusAAAProxyNumIncmpltAuth=_RuckusAAAProxyNumIncmpltAuth_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,4),_RuckusAAAProxyNumIncmpltAuth_Type())
ruckusAAAProxyNumIncmpltAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumIncmpltAuth.setStatus(_A)
_RuckusAAAProxyNumSuccAcc_Type=Counter64
_RuckusAAAProxyNumSuccAcc_Object=MibTableColumn
ruckusAAAProxyNumSuccAcc=_RuckusAAAProxyNumSuccAcc_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,5),_RuckusAAAProxyNumSuccAcc_Type())
ruckusAAAProxyNumSuccAcc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumSuccAcc.setStatus(_A)
_RuckusAAAProxyNumFailAcc_Type=Counter64
_RuckusAAAProxyNumFailAcc_Object=MibTableColumn
ruckusAAAProxyNumFailAcc=_RuckusAAAProxyNumFailAcc_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,6),_RuckusAAAProxyNumFailAcc_Type())
ruckusAAAProxyNumFailAcc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumFailAcc.setStatus(_A)
_RuckusAAAProxyNumAcsRqRcvdNas_Type=Counter64
_RuckusAAAProxyNumAcsRqRcvdNas_Object=MibTableColumn
ruckusAAAProxyNumAcsRqRcvdNas=_RuckusAAAProxyNumAcsRqRcvdNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,7),_RuckusAAAProxyNumAcsRqRcvdNas_Type())
ruckusAAAProxyNumAcsRqRcvdNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsRqRcvdNas.setStatus(_A)
_RuckusAAAProxyNumAcsRqSntAaa_Type=Counter64
_RuckusAAAProxyNumAcsRqSntAaa_Object=MibTableColumn
ruckusAAAProxyNumAcsRqSntAaa=_RuckusAAAProxyNumAcsRqSntAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,8),_RuckusAAAProxyNumAcsRqSntAaa_Type())
ruckusAAAProxyNumAcsRqSntAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsRqSntAaa.setStatus(_A)
_RuckusAAAProxyNumAcsChRcvdAaa_Type=Counter64
_RuckusAAAProxyNumAcsChRcvdAaa_Object=MibTableColumn
ruckusAAAProxyNumAcsChRcvdAaa=_RuckusAAAProxyNumAcsChRcvdAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,9),_RuckusAAAProxyNumAcsChRcvdAaa_Type())
ruckusAAAProxyNumAcsChRcvdAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsChRcvdAaa.setStatus(_A)
_RuckusAAAProxyNumAcsChSntNas_Type=Counter64
_RuckusAAAProxyNumAcsChSntNas_Object=MibTableColumn
ruckusAAAProxyNumAcsChSntNas=_RuckusAAAProxyNumAcsChSntNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,10),_RuckusAAAProxyNumAcsChSntNas_Type())
ruckusAAAProxyNumAcsChSntNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsChSntNas.setStatus(_A)
_RuckusAAAProxyNumAcsAcpRcvdAaa_Type=Counter64
_RuckusAAAProxyNumAcsAcpRcvdAaa_Object=MibTableColumn
ruckusAAAProxyNumAcsAcpRcvdAaa=_RuckusAAAProxyNumAcsAcpRcvdAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,11),_RuckusAAAProxyNumAcsAcpRcvdAaa_Type())
ruckusAAAProxyNumAcsAcpRcvdAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsAcpRcvdAaa.setStatus(_A)
_RuckusAAAProxyNumAcsAcpSntNas_Type=Counter64
_RuckusAAAProxyNumAcsAcpSntNas_Object=MibTableColumn
ruckusAAAProxyNumAcsAcpSntNas=_RuckusAAAProxyNumAcsAcpSntNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,12),_RuckusAAAProxyNumAcsAcpSntNas_Type())
ruckusAAAProxyNumAcsAcpSntNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsAcpSntNas.setStatus(_A)
_RuckusAAAProxyNumAcsRejRcvdAaa_Type=Counter64
_RuckusAAAProxyNumAcsRejRcvdAaa_Object=MibTableColumn
ruckusAAAProxyNumAcsRejRcvdAaa=_RuckusAAAProxyNumAcsRejRcvdAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,13),_RuckusAAAProxyNumAcsRejRcvdAaa_Type())
ruckusAAAProxyNumAcsRejRcvdAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsRejRcvdAaa.setStatus(_A)
_RuckusAAAProxyNumAcsRejSntNas_Type=Counter64
_RuckusAAAProxyNumAcsRejSntNas_Object=MibTableColumn
ruckusAAAProxyNumAcsRejSntNas=_RuckusAAAProxyNumAcsRejSntNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,14),_RuckusAAAProxyNumAcsRejSntNas_Type())
ruckusAAAProxyNumAcsRejSntNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAcsRejSntNas.setStatus(_A)
_RuckusAAAProxyNumAccRqRcvdNas_Type=Counter64
_RuckusAAAProxyNumAccRqRcvdNas_Object=MibTableColumn
ruckusAAAProxyNumAccRqRcvdNas=_RuckusAAAProxyNumAccRqRcvdNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,15),_RuckusAAAProxyNumAccRqRcvdNas_Type())
ruckusAAAProxyNumAccRqRcvdNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAccRqRcvdNas.setStatus(_A)
_RuckusAAAProxyNumAccRqSntAaa_Type=Counter64
_RuckusAAAProxyNumAccRqSntAaa_Object=MibTableColumn
ruckusAAAProxyNumAccRqSntAaa=_RuckusAAAProxyNumAccRqSntAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,16),_RuckusAAAProxyNumAccRqSntAaa_Type())
ruckusAAAProxyNumAccRqSntAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAccRqSntAaa.setStatus(_A)
_RuckusAAAProxyNumAccRspRcdAaa_Type=Counter64
_RuckusAAAProxyNumAccRspRcdAaa_Object=MibTableColumn
ruckusAAAProxyNumAccRspRcdAaa=_RuckusAAAProxyNumAccRspRcdAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,17),_RuckusAAAProxyNumAccRspRcdAaa_Type())
ruckusAAAProxyNumAccRspRcdAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAccRspRcdAaa.setStatus(_A)
_RuckusAAAProxyNumAccRspSntNas_Type=Counter64
_RuckusAAAProxyNumAccRspSntNas_Object=MibTableColumn
ruckusAAAProxyNumAccRspSntNas=_RuckusAAAProxyNumAccRspSntNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,18),_RuckusAAAProxyNumAccRspSntNas_Type())
ruckusAAAProxyNumAccRspSntNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumAccRspSntNas.setStatus(_A)
_RuckusAAAProxyNumCoaRcvdAaa_Type=Counter64
_RuckusAAAProxyNumCoaRcvdAaa_Object=MibTableColumn
ruckusAAAProxyNumCoaRcvdAaa=_RuckusAAAProxyNumCoaRcvdAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,19),_RuckusAAAProxyNumCoaRcvdAaa_Type())
ruckusAAAProxyNumCoaRcvdAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumCoaRcvdAaa.setStatus(_A)
_RuckusAAAProxyNumCoaSucSntAaa_Type=Counter64
_RuckusAAAProxyNumCoaSucSntAaa_Object=MibTableColumn
ruckusAAAProxyNumCoaSucSntAaa=_RuckusAAAProxyNumCoaSucSntAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,20),_RuckusAAAProxyNumCoaSucSntAaa_Type())
ruckusAAAProxyNumCoaSucSntAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumCoaSucSntAaa.setStatus(_A)
_RuckusAAAProxyNumCoaFailSntAaa_Type=Counter64
_RuckusAAAProxyNumCoaFailSntAaa_Object=MibTableColumn
ruckusAAAProxyNumCoaFailSntAaa=_RuckusAAAProxyNumCoaFailSntAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,21),_RuckusAAAProxyNumCoaFailSntAaa_Type())
ruckusAAAProxyNumCoaFailSntAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumCoaFailSntAaa.setStatus(_A)
_RuckusAAAProxyNumDmRcvdAaa_Type=Counter64
_RuckusAAAProxyNumDmRcvdAaa_Object=MibTableColumn
ruckusAAAProxyNumDmRcvdAaa=_RuckusAAAProxyNumDmRcvdAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,22),_RuckusAAAProxyNumDmRcvdAaa_Type())
ruckusAAAProxyNumDmRcvdAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumDmRcvdAaa.setStatus(_A)
_RuckusAAAProxyNumDmSntNas_Type=Counter64
_RuckusAAAProxyNumDmSntNas_Object=MibTableColumn
ruckusAAAProxyNumDmSntNas=_RuckusAAAProxyNumDmSntNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,23),_RuckusAAAProxyNumDmSntNas_Type())
ruckusAAAProxyNumDmSntNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumDmSntNas.setStatus(_A)
_RuckusAAAProxyNumDmSucRcdNas_Type=Counter64
_RuckusAAAProxyNumDmSucRcdNas_Object=MibTableColumn
ruckusAAAProxyNumDmSucRcdNas=_RuckusAAAProxyNumDmSucRcdNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,24),_RuckusAAAProxyNumDmSucRcdNas_Type())
ruckusAAAProxyNumDmSucRcdNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumDmSucRcdNas.setStatus(_A)
_RuckusAAAProxyNumDmSucSntAaa_Type=Counter64
_RuckusAAAProxyNumDmSucSntAaa_Object=MibTableColumn
ruckusAAAProxyNumDmSucSntAaa=_RuckusAAAProxyNumDmSucSntAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,25),_RuckusAAAProxyNumDmSucSntAaa_Type())
ruckusAAAProxyNumDmSucSntAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumDmSucSntAaa.setStatus(_A)
_RuckusAAAProxyNumDmFailRcdNas_Type=Counter64
_RuckusAAAProxyNumDmFailRcdNas_Object=MibTableColumn
ruckusAAAProxyNumDmFailRcdNas=_RuckusAAAProxyNumDmFailRcdNas_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,26),_RuckusAAAProxyNumDmFailRcdNas_Type())
ruckusAAAProxyNumDmFailRcdNas.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumDmFailRcdNas.setStatus(_A)
_RuckusAAAProxyNumDmFailSntAaa_Type=Counter64
_RuckusAAAProxyNumDmFailSntAaa_Object=MibTableColumn
ruckusAAAProxyNumDmFailSntAaa=_RuckusAAAProxyNumDmFailSntAaa_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,27),_RuckusAAAProxyNumDmFailSntAaa_Type())
ruckusAAAProxyNumDmFailSntAaa.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyNumDmFailSntAaa.setStatus(_A)
_RuckusAAAProxyIndex_Type=Integer32
_RuckusAAAProxyIndex_Object=MibTableColumn
ruckusAAAProxyIndex=_RuckusAAAProxyIndex_Object((1,3,6,1,4,1,25053,1,3,3,1,1,2,1,1,99),_RuckusAAAProxyIndex_Type())
ruckusAAAProxyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusAAAProxyIndex.setStatus(_A)
_RuckusCGFInfo_ObjectIdentity=ObjectIdentity
ruckusCGFInfo=_RuckusCGFInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,3,3,1,1,3))
_RuckusCGFTable_Object=MibTable
ruckusCGFTable=_RuckusCGFTable_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1))
if mibBuilder.loadTexts:ruckusCGFTable.setStatus(_A)
_RuckusCGFEntry_Object=MibTableRow
ruckusCGFEntry=_RuckusCGFEntry_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1))
ruckusCGFEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:ruckusCGFEntry.setStatus(_A)
_RuckusCGFCgfSrvcName_Type=DisplayString
_RuckusCGFCgfSrvcName_Object=MibTableColumn
ruckusCGFCgfSrvcName=_RuckusCGFCgfSrvcName_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,1),_RuckusCGFCgfSrvcName_Type())
ruckusCGFCgfSrvcName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFCgfSrvcName.setStatus(_A)
_RuckusCGFCgfIp_Type=DisplayString
_RuckusCGFCgfIp_Object=MibTableColumn
ruckusCGFCgfIp=_RuckusCGFCgfIp_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,2),_RuckusCGFCgfIp_Type())
ruckusCGFCgfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFCgfIp.setStatus(_A)
_RuckusCGFNumSuccCdrTxfd_Type=Counter64
_RuckusCGFNumSuccCdrTxfd_Object=MibTableColumn
ruckusCGFNumSuccCdrTxfd=_RuckusCGFNumSuccCdrTxfd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,3),_RuckusCGFNumSuccCdrTxfd_Type())
ruckusCGFNumSuccCdrTxfd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumSuccCdrTxfd.setStatus(_A)
_RuckusCGFNumCdrTxfrFail_Type=Counter64
_RuckusCGFNumCdrTxfrFail_Object=MibTableColumn
ruckusCGFNumCdrTxfrFail=_RuckusCGFNumCdrTxfrFail_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,4),_RuckusCGFNumCdrTxfrFail_Type())
ruckusCGFNumCdrTxfrFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumCdrTxfrFail.setStatus(_A)
_RuckusCGFNumCdrPossDup_Type=Counter64
_RuckusCGFNumCdrPossDup_Object=MibTableColumn
ruckusCGFNumCdrPossDup=_RuckusCGFNumCdrPossDup_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,5),_RuckusCGFNumCdrPossDup_Type())
ruckusCGFNumCdrPossDup.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumCdrPossDup.setStatus(_A)
_RuckusCGFNumCdrRlsReq_Type=Counter64
_RuckusCGFNumCdrRlsReq_Object=MibTableColumn
ruckusCGFNumCdrRlsReq=_RuckusCGFNumCdrRlsReq_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,6),_RuckusCGFNumCdrRlsReq_Type())
ruckusCGFNumCdrRlsReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumCdrRlsReq.setStatus(_A)
_RuckusCGFNumCdrCnclReq_Type=Counter64
_RuckusCGFNumCdrCnclReq_Object=MibTableColumn
ruckusCGFNumCdrCnclReq=_RuckusCGFNumCdrCnclReq_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,7),_RuckusCGFNumCdrCnclReq_Type())
ruckusCGFNumCdrCnclReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumCdrCnclReq.setStatus(_A)
_RuckusCGFNumDrtrReqSnt_Type=Counter64
_RuckusCGFNumDrtrReqSnt_Object=MibTableColumn
ruckusCGFNumDrtrReqSnt=_RuckusCGFNumDrtrReqSnt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,8),_RuckusCGFNumDrtrReqSnt_Type())
ruckusCGFNumDrtrReqSnt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumDrtrReqSnt.setStatus(_A)
_RuckusCGFNumDrtrSucRspRcvd_Type=Counter64
_RuckusCGFNumDrtrSucRspRcvd_Object=MibTableColumn
ruckusCGFNumDrtrSucRspRcvd=_RuckusCGFNumDrtrSucRspRcvd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,9),_RuckusCGFNumDrtrSucRspRcvd_Type())
ruckusCGFNumDrtrSucRspRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumDrtrSucRspRcvd.setStatus(_A)
_RuckusCGFNumDrtrFailRspRcvd_Type=Counter64
_RuckusCGFNumDrtrFailRspRcvd_Object=MibTableColumn
ruckusCGFNumDrtrFailRspRcvd=_RuckusCGFNumDrtrFailRspRcvd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,10),_RuckusCGFNumDrtrFailRspRcvd_Type())
ruckusCGFNumDrtrFailRspRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFNumDrtrFailRspRcvd.setStatus(_A)
_RuckusCGFIndex_Type=Integer32
_RuckusCGFIndex_Object=MibTableColumn
ruckusCGFIndex=_RuckusCGFIndex_Object((1,3,6,1,4,1,25053,1,3,3,1,1,3,1,1,99),_RuckusCGFIndex_Type())
ruckusCGFIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusCGFIndex.setStatus(_A)
_RuckusGTPUInfo_ObjectIdentity=ObjectIdentity
ruckusGTPUInfo=_RuckusGTPUInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,3,3,1,1,4))
_RuckusGTPUTable_Object=MibTable
ruckusGTPUTable=_RuckusGTPUTable_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1))
if mibBuilder.loadTexts:ruckusGTPUTable.setStatus(_A)
_RuckusGTPUEntry_Object=MibTableRow
ruckusGTPUEntry=_RuckusGTPUEntry_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1))
ruckusGTPUEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:ruckusGTPUEntry.setStatus(_A)
_RuckusGTPUGgsnIPAddr_Type=DisplayString
_RuckusGTPUGgsnIPAddr_Object=MibTableColumn
ruckusGTPUGgsnIPAddr=_RuckusGTPUGgsnIPAddr_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,1),_RuckusGTPUGgsnIPAddr_Type())
ruckusGTPUGgsnIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUGgsnIPAddr.setStatus(_A)
_RuckusGTPUTxPkts_Type=Counter64
_RuckusGTPUTxPkts_Object=MibTableColumn
ruckusGTPUTxPkts=_RuckusGTPUTxPkts_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,2),_RuckusGTPUTxPkts_Type())
ruckusGTPUTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUTxPkts.setStatus(_A)
_RuckusGTPUTxBytes_Type=Counter64
_RuckusGTPUTxBytes_Object=MibTableColumn
ruckusGTPUTxBytes=_RuckusGTPUTxBytes_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,3),_RuckusGTPUTxBytes_Type())
ruckusGTPUTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUTxBytes.setStatus(_A)
_RuckusGTPURxPkts_Type=Counter64
_RuckusGTPURxPkts_Object=MibTableColumn
ruckusGTPURxPkts=_RuckusGTPURxPkts_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,4),_RuckusGTPURxPkts_Type())
ruckusGTPURxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPURxPkts.setStatus(_A)
_RuckusGTPURxBytes_Type=Counter64
_RuckusGTPURxBytes_Object=MibTableColumn
ruckusGTPURxBytes=_RuckusGTPURxBytes_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,5),_RuckusGTPURxBytes_Type())
ruckusGTPURxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPURxBytes.setStatus(_A)
_RuckusGTPUTxDrops_Type=Counter64
_RuckusGTPUTxDrops_Object=MibTableColumn
ruckusGTPUTxDrops=_RuckusGTPUTxDrops_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,6),_RuckusGTPUTxDrops_Type())
ruckusGTPUTxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUTxDrops.setStatus(_A)
_RuckusGTPURxDrops_Type=Counter64
_RuckusGTPURxDrops_Object=MibTableColumn
ruckusGTPURxDrops=_RuckusGTPURxDrops_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,7),_RuckusGTPURxDrops_Type())
ruckusGTPURxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPURxDrops.setStatus(_A)
_RuckusGTPUNumBadGTPU_Type=Counter64
_RuckusGTPUNumBadGTPU_Object=MibTableColumn
ruckusGTPUNumBadGTPU=_RuckusGTPUNumBadGTPU_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,8),_RuckusGTPUNumBadGTPU_Type())
ruckusGTPUNumBadGTPU.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUNumBadGTPU.setStatus(_A)
_RuckusGTPUNumRXTeidInvalid_Type=Counter64
_RuckusGTPUNumRXTeidInvalid_Object=MibTableColumn
ruckusGTPUNumRXTeidInvalid=_RuckusGTPUNumRXTeidInvalid_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,9),_RuckusGTPUNumRXTeidInvalid_Type())
ruckusGTPUNumRXTeidInvalid.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUNumRXTeidInvalid.setStatus(_A)
_RuckusGTPUNumTXTeidInvalid_Type=Counter64
_RuckusGTPUNumTXTeidInvalid_Object=MibTableColumn
ruckusGTPUNumTXTeidInvalid=_RuckusGTPUNumTXTeidInvalid_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,10),_RuckusGTPUNumTXTeidInvalid_Type())
ruckusGTPUNumTXTeidInvalid.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUNumTXTeidInvalid.setStatus(_A)
_RuckusGTPUNumOfEchoRX_Type=Counter64
_RuckusGTPUNumOfEchoRX_Object=MibTableColumn
ruckusGTPUNumOfEchoRX=_RuckusGTPUNumOfEchoRX_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,11),_RuckusGTPUNumOfEchoRX_Type())
ruckusGTPUNumOfEchoRX.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUNumOfEchoRX.setStatus(_A)
_RuckusGTPUIndex_Type=Integer32
_RuckusGTPUIndex_Object=MibTableColumn
ruckusGTPUIndex=_RuckusGTPUIndex_Object((1,3,6,1,4,1,25053,1,3,3,1,1,4,1,1,99),_RuckusGTPUIndex_Type())
ruckusGTPUIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGTPUIndex.setStatus(_A)
_RuckusGGSNGTPCInfo_ObjectIdentity=ObjectIdentity
ruckusGGSNGTPCInfo=_RuckusGGSNGTPCInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,3,3,1,1,5))
_RuckusGGSNGTPCTable_Object=MibTable
ruckusGGSNGTPCTable=_RuckusGGSNGTPCTable_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1))
if mibBuilder.loadTexts:ruckusGGSNGTPCTable.setStatus(_A)
_RuckusGGSNGTPCEntry_Object=MibTableRow
ruckusGGSNGTPCEntry=_RuckusGGSNGTPCEntry_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1))
ruckusGGSNGTPCEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:ruckusGGSNGTPCEntry.setStatus(_A)
_RuckusGGSNGTPCGgsnIp_Type=DisplayString
_RuckusGGSNGTPCGgsnIp_Object=MibTableColumn
ruckusGGSNGTPCGgsnIp=_RuckusGGSNGTPCGgsnIp_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,1),_RuckusGGSNGTPCGgsnIp_Type())
ruckusGGSNGTPCGgsnIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCGgsnIp.setStatus(_A)
_RuckusGGSNGTPCNumActPdp_Type=Counter64
_RuckusGGSNGTPCNumActPdp_Object=MibTableColumn
ruckusGGSNGTPCNumActPdp=_RuckusGGSNGTPCNumActPdp_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,2),_RuckusGGSNGTPCNumActPdp_Type())
ruckusGGSNGTPCNumActPdp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCNumActPdp.setStatus(_A)
_RuckusGGSNGTPCSuccPdpCrt_Type=Counter64
_RuckusGGSNGTPCSuccPdpCrt_Object=MibTableColumn
ruckusGGSNGTPCSuccPdpCrt=_RuckusGGSNGTPCSuccPdpCrt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,3),_RuckusGGSNGTPCSuccPdpCrt_Type())
ruckusGGSNGTPCSuccPdpCrt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccPdpCrt.setStatus(_A)
_RuckusGGSNGTPCFailPdpCrt_Type=Counter64
_RuckusGGSNGTPCFailPdpCrt_Object=MibTableColumn
ruckusGGSNGTPCFailPdpCrt=_RuckusGGSNGTPCFailPdpCrt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,4),_RuckusGGSNGTPCFailPdpCrt_Type())
ruckusGGSNGTPCFailPdpCrt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailPdpCrt.setStatus(_A)
_RuckusGGSNGTPCSuccPdpUpdRcvd_Type=Counter64
_RuckusGGSNGTPCSuccPdpUpdRcvd_Object=MibTableColumn
ruckusGGSNGTPCSuccPdpUpdRcvd=_RuckusGGSNGTPCSuccPdpUpdRcvd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,5),_RuckusGGSNGTPCSuccPdpUpdRcvd_Type())
ruckusGGSNGTPCSuccPdpUpdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccPdpUpdRcvd.setStatus(_A)
_RuckusGGSNGTPCFailPdpUpdRcvd_Type=Counter64
_RuckusGGSNGTPCFailPdpUpdRcvd_Object=MibTableColumn
ruckusGGSNGTPCFailPdpUpdRcvd=_RuckusGGSNGTPCFailPdpUpdRcvd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,6),_RuckusGGSNGTPCFailPdpUpdRcvd_Type())
ruckusGGSNGTPCFailPdpUpdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailPdpUpdRcvd.setStatus(_A)
_RuckusGGSNGTPCSuccPdpUpdInitRM_Type=Counter64
_RuckusGGSNGTPCSuccPdpUpdInitRM_Object=MibTableColumn
ruckusGGSNGTPCSuccPdpUpdInitRM=_RuckusGGSNGTPCSuccPdpUpdInitRM_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,7),_RuckusGGSNGTPCSuccPdpUpdInitRM_Type())
ruckusGGSNGTPCSuccPdpUpdInitRM.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccPdpUpdInitRM.setStatus(_A)
_RuckusGGSNGTPCFailPdpUpdInitRM_Type=Counter64
_RuckusGGSNGTPCFailPdpUpdInitRM_Object=MibTableColumn
ruckusGGSNGTPCFailPdpUpdInitRM=_RuckusGGSNGTPCFailPdpUpdInitRM_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,8),_RuckusGGSNGTPCFailPdpUpdInitRM_Type())
ruckusGGSNGTPCFailPdpUpdInitRM.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailPdpUpdInitRM.setStatus(_A)
_RuckusGGSNGTPCSuccPdpUpdInitAAA_Type=Counter64
_RuckusGGSNGTPCSuccPdpUpdInitAAA_Object=MibTableColumn
ruckusGGSNGTPCSuccPdpUpdInitAAA=_RuckusGGSNGTPCSuccPdpUpdInitAAA_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,9),_RuckusGGSNGTPCSuccPdpUpdInitAAA_Type())
ruckusGGSNGTPCSuccPdpUpdInitAAA.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccPdpUpdInitAAA.setStatus(_A)
_RuckusGGSNGTPCFailPdpUpdInitAAA_Type=Counter64
_RuckusGGSNGTPCFailPdpUpdInitAAA_Object=MibTableColumn
ruckusGGSNGTPCFailPdpUpdInitAAA=_RuckusGGSNGTPCFailPdpUpdInitAAA_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,10),_RuckusGGSNGTPCFailPdpUpdInitAAA_Type())
ruckusGGSNGTPCFailPdpUpdInitAAA.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailPdpUpdInitAAA.setStatus(_A)
_RuckusGGSNGTPCSuccPdpUpdInitHLR_Type=Counter64
_RuckusGGSNGTPCSuccPdpUpdInitHLR_Object=MibTableColumn
ruckusGGSNGTPCSuccPdpUpdInitHLR=_RuckusGGSNGTPCSuccPdpUpdInitHLR_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,11),_RuckusGGSNGTPCSuccPdpUpdInitHLR_Type())
ruckusGGSNGTPCSuccPdpUpdInitHLR.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccPdpUpdInitHLR.setStatus(_A)
_RuckusGGSNGTPCFailPdpUpdInitHLR_Type=Counter64
_RuckusGGSNGTPCFailPdpUpdInitHLR_Object=MibTableColumn
ruckusGGSNGTPCFailPdpUpdInitHLR=_RuckusGGSNGTPCFailPdpUpdInitHLR_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,12),_RuckusGGSNGTPCFailPdpUpdInitHLR_Type())
ruckusGGSNGTPCFailPdpUpdInitHLR.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailPdpUpdInitHLR.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpRcvd_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpRcvd_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpRcvd=_RuckusGGSNGTPCSuccDelPdpRcvd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,13),_RuckusGGSNGTPCSuccDelPdpRcvd_Type())
ruckusGGSNGTPCSuccDelPdpRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpRcvd.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpRcvd_Type=Counter64
_RuckusGGSNGTPCFailDelPdpRcvd_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpRcvd=_RuckusGGSNGTPCFailDelPdpRcvd_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,14),_RuckusGGSNGTPCFailDelPdpRcvd_Type())
ruckusGGSNGTPCFailDelPdpRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpRcvd.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpInitErr_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpInitErr_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitErr=_RuckusGGSNGTPCSuccDelPdpInitErr_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,15),_RuckusGGSNGTPCSuccDelPdpInitErr_Type())
ruckusGGSNGTPCSuccDelPdpInitErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpInitErr.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpInitErr_Type=Counter64
_RuckusGGSNGTPCFailDelPdpInitErr_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpInitErr=_RuckusGGSNGTPCFailDelPdpInitErr_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,16),_RuckusGGSNGTPCFailDelPdpInitErr_Type())
ruckusGGSNGTPCFailDelPdpInitErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpInitErr.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpInitDM_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpInitDM_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitDM=_RuckusGGSNGTPCSuccDelPdpInitDM_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,17),_RuckusGGSNGTPCSuccDelPdpInitDM_Type())
ruckusGGSNGTPCSuccDelPdpInitDM.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpInitDM.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpInitDM_Type=Counter64
_RuckusGGSNGTPCFailDelPdpInitDM_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpInitDM=_RuckusGGSNGTPCFailDelPdpInitDM_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,18),_RuckusGGSNGTPCFailDelPdpInitDM_Type())
ruckusGGSNGTPCFailDelPdpInitDM.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpInitDM.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpInitHLR_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpInitHLR_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitHLR=_RuckusGGSNGTPCSuccDelPdpInitHLR_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,19),_RuckusGGSNGTPCSuccDelPdpInitHLR_Type())
ruckusGGSNGTPCSuccDelPdpInitHLR.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpInitHLR.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpInitHLR_Type=Counter64
_RuckusGGSNGTPCFailDelPdpInitHLR_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpInitHLR=_RuckusGGSNGTPCFailDelPdpInitHLR_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,20),_RuckusGGSNGTPCFailDelPdpInitHLR_Type())
ruckusGGSNGTPCFailDelPdpInitHLR.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpInitHLR.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpInitSCG_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpInitSCG_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitSCG=_RuckusGGSNGTPCSuccDelPdpInitSCG_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,21),_RuckusGGSNGTPCSuccDelPdpInitSCG_Type())
ruckusGGSNGTPCSuccDelPdpInitSCG.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpInitSCG.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpInitSCG_Type=Counter64
_RuckusGGSNGTPCFailDelPdpInitSCG_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpInitSCG=_RuckusGGSNGTPCFailDelPdpInitSCG_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,22),_RuckusGGSNGTPCFailDelPdpInitSCG_Type())
ruckusGGSNGTPCFailDelPdpInitSCG.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpInitSCG.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpInitAP_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpInitAP_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitAP=_RuckusGGSNGTPCSuccDelPdpInitAP_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,23),_RuckusGGSNGTPCSuccDelPdpInitAP_Type())
ruckusGGSNGTPCSuccDelPdpInitAP.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpInitAP.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpInitAP_Type=Counter64
_RuckusGGSNGTPCFailDelPdpInitAP_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpInitAP=_RuckusGGSNGTPCFailDelPdpInitAP_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,24),_RuckusGGSNGTPCFailDelPdpInitAP_Type())
ruckusGGSNGTPCFailDelPdpInitAP.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpInitAP.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpInitD_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpInitD_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitD=_RuckusGGSNGTPCSuccDelPdpInitD_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,25),_RuckusGGSNGTPCSuccDelPdpInitD_Type())
ruckusGGSNGTPCSuccDelPdpInitD.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpInitD.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpInitD_Type=Counter64
_RuckusGGSNGTPCFailDelPdpInitD_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpInitD=_RuckusGGSNGTPCFailDelPdpInitD_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,26),_RuckusGGSNGTPCFailDelPdpInitD_Type())
ruckusGGSNGTPCFailDelPdpInitD.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpInitD.setStatus(_A)
_RuckusGGSNGTPCSuccDelPdpInitClnt_Type=Counter64
_RuckusGGSNGTPCSuccDelPdpInitClnt_Object=MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitClnt=_RuckusGGSNGTPCSuccDelPdpInitClnt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,27),_RuckusGGSNGTPCSuccDelPdpInitClnt_Type())
ruckusGGSNGTPCSuccDelPdpInitClnt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCSuccDelPdpInitClnt.setStatus(_A)
_RuckusGGSNGTPCFailDelPdpInitClnt_Type=Counter64
_RuckusGGSNGTPCFailDelPdpInitClnt_Object=MibTableColumn
ruckusGGSNGTPCFailDelPdpInitClnt=_RuckusGGSNGTPCFailDelPdpInitClnt_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,28),_RuckusGGSNGTPCFailDelPdpInitClnt_Type())
ruckusGGSNGTPCFailDelPdpInitClnt.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCFailDelPdpInitClnt.setStatus(_A)
_RuckusGGSNGTPCIndex_Type=Integer32
_RuckusGGSNGTPCIndex_Object=MibTableColumn
ruckusGGSNGTPCIndex=_RuckusGGSNGTPCIndex_Object((1,3,6,1,4,1,25053,1,3,3,1,1,5,1,1,99),_RuckusGGSNGTPCIndex_Type())
ruckusGGSNGTPCIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusGGSNGTPCIndex.setStatus(_A)
_RuckusHLRInfo_ObjectIdentity=ObjectIdentity
ruckusHLRInfo=_RuckusHLRInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,3,3,1,1,7))
_RuckusHLRTable_Object=MibTable
ruckusHLRTable=_RuckusHLRTable_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1))
if mibBuilder.loadTexts:ruckusHLRTable.setStatus(_A)
_RuckusHLREntry_Object=MibTableRow
ruckusHLREntry=_RuckusHLREntry_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1))
ruckusHLREntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:ruckusHLREntry.setStatus(_A)
_RuckusHLRHlrSrvcName_Type=DisplayString
_RuckusHLRHlrSrvcName_Object=MibTableColumn
ruckusHLRHlrSrvcName=_RuckusHLRHlrSrvcName_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,1),_RuckusHLRHlrSrvcName_Type())
ruckusHLRHlrSrvcName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRHlrSrvcName.setStatus(_A)
_RuckusHLRNumSucAuthInfoReqSim_Type=Counter64
_RuckusHLRNumSucAuthInfoReqSim_Object=MibTableColumn
ruckusHLRNumSucAuthInfoReqSim=_RuckusHLRNumSucAuthInfoReqSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,2),_RuckusHLRNumSucAuthInfoReqSim_Type())
ruckusHLRNumSucAuthInfoReqSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumSucAuthInfoReqSim.setStatus(_A)
_RuckusHLRNumAuthInfoRqErrHlrSim_Type=Counter64
_RuckusHLRNumAuthInfoRqErrHlrSim_Object=MibTableColumn
ruckusHLRNumAuthInfoRqErrHlrSim=_RuckusHLRNumAuthInfoRqErrHlrSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,3),_RuckusHLRNumAuthInfoRqErrHlrSim_Type())
ruckusHLRNumAuthInfoRqErrHlrSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumAuthInfoRqErrHlrSim.setStatus(_A)
_RuckusHLRNumAuthInfoRqTmotSim_Type=Counter64
_RuckusHLRNumAuthInfoRqTmotSim_Object=MibTableColumn
ruckusHLRNumAuthInfoRqTmotSim=_RuckusHLRNumAuthInfoRqTmotSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,4),_RuckusHLRNumAuthInfoRqTmotSim_Type())
ruckusHLRNumAuthInfoRqTmotSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumAuthInfoRqTmotSim.setStatus(_A)
_RuckusHLRNumSucAuthInfoReqAka_Type=Counter64
_RuckusHLRNumSucAuthInfoReqAka_Object=MibTableColumn
ruckusHLRNumSucAuthInfoReqAka=_RuckusHLRNumSucAuthInfoReqAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,5),_RuckusHLRNumSucAuthInfoReqAka_Type())
ruckusHLRNumSucAuthInfoReqAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumSucAuthInfoReqAka.setStatus(_A)
_RuckusHLRNumAuthInfoRqErrHlrAka_Type=Counter64
_RuckusHLRNumAuthInfoRqErrHlrAka_Object=MibTableColumn
ruckusHLRNumAuthInfoRqErrHlrAka=_RuckusHLRNumAuthInfoRqErrHlrAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,6),_RuckusHLRNumAuthInfoRqErrHlrAka_Type())
ruckusHLRNumAuthInfoRqErrHlrAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumAuthInfoRqErrHlrAka.setStatus(_A)
_RuckusHLRNumAuthInfoRqTmotAka_Type=Counter64
_RuckusHLRNumAuthInfoRqTmotAka_Object=MibTableColumn
ruckusHLRNumAuthInfoRqTmotAka=_RuckusHLRNumAuthInfoRqTmotAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,7),_RuckusHLRNumAuthInfoRqTmotAka_Type())
ruckusHLRNumAuthInfoRqTmotAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumAuthInfoRqTmotAka.setStatus(_A)
_RuckusHLRNumUpdGprsSuccSim_Type=Counter64
_RuckusHLRNumUpdGprsSuccSim_Object=MibTableColumn
ruckusHLRNumUpdGprsSuccSim=_RuckusHLRNumUpdGprsSuccSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,8),_RuckusHLRNumUpdGprsSuccSim_Type())
ruckusHLRNumUpdGprsSuccSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumUpdGprsSuccSim.setStatus(_A)
_RuckusHLRNumUpdGprsFailErrSim_Type=Counter64
_RuckusHLRNumUpdGprsFailErrSim_Object=MibTableColumn
ruckusHLRNumUpdGprsFailErrSim=_RuckusHLRNumUpdGprsFailErrSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,9),_RuckusHLRNumUpdGprsFailErrSim_Type())
ruckusHLRNumUpdGprsFailErrSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumUpdGprsFailErrSim.setStatus(_A)
_RuckusHLRNumUpdGprsFailTmoSim_Type=Counter64
_RuckusHLRNumUpdGprsFailTmoSim_Object=MibTableColumn
ruckusHLRNumUpdGprsFailTmoSim=_RuckusHLRNumUpdGprsFailTmoSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,10),_RuckusHLRNumUpdGprsFailTmoSim_Type())
ruckusHLRNumUpdGprsFailTmoSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumUpdGprsFailTmoSim.setStatus(_A)
_RuckusHLRNumUpdGprsSuccAka_Type=Counter64
_RuckusHLRNumUpdGprsSuccAka_Object=MibTableColumn
ruckusHLRNumUpdGprsSuccAka=_RuckusHLRNumUpdGprsSuccAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,11),_RuckusHLRNumUpdGprsSuccAka_Type())
ruckusHLRNumUpdGprsSuccAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumUpdGprsSuccAka.setStatus(_A)
_RuckusHLRNumUpdGprsFailErrAka_Type=Counter64
_RuckusHLRNumUpdGprsFailErrAka_Object=MibTableColumn
ruckusHLRNumUpdGprsFailErrAka=_RuckusHLRNumUpdGprsFailErrAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,12),_RuckusHLRNumUpdGprsFailErrAka_Type())
ruckusHLRNumUpdGprsFailErrAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumUpdGprsFailErrAka.setStatus(_A)
_RuckusHLRNumUpdGprsFailTmoAka_Type=Counter64
_RuckusHLRNumUpdGprsFailTmoAka_Object=MibTableColumn
ruckusHLRNumUpdGprsFailTmoAka=_RuckusHLRNumUpdGprsFailTmoAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,13),_RuckusHLRNumUpdGprsFailTmoAka_Type())
ruckusHLRNumUpdGprsFailTmoAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumUpdGprsFailTmoAka.setStatus(_A)
_RuckusHLRNumRstDtaSuccSim_Type=Counter64
_RuckusHLRNumRstDtaSuccSim_Object=MibTableColumn
ruckusHLRNumRstDtaSuccSim=_RuckusHLRNumRstDtaSuccSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,14),_RuckusHLRNumRstDtaSuccSim_Type())
ruckusHLRNumRstDtaSuccSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumRstDtaSuccSim.setStatus(_A)
_RuckusHLRNumRstDtaFailErrHlrSim_Type=Counter64
_RuckusHLRNumRstDtaFailErrHlrSim_Object=MibTableColumn
ruckusHLRNumRstDtaFailErrHlrSim=_RuckusHLRNumRstDtaFailErrHlrSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,15),_RuckusHLRNumRstDtaFailErrHlrSim_Type())
ruckusHLRNumRstDtaFailErrHlrSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumRstDtaFailErrHlrSim.setStatus(_A)
_RuckusHLRNumRstDtaFailTmoSim_Type=Counter64
_RuckusHLRNumRstDtaFailTmoSim_Object=MibTableColumn
ruckusHLRNumRstDtaFailTmoSim=_RuckusHLRNumRstDtaFailTmoSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,16),_RuckusHLRNumRstDtaFailTmoSim_Type())
ruckusHLRNumRstDtaFailTmoSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumRstDtaFailTmoSim.setStatus(_A)
_RuckusHLRNumRstDtaSuccAka_Type=Counter64
_RuckusHLRNumRstDtaSuccAka_Object=MibTableColumn
ruckusHLRNumRstDtaSuccAka=_RuckusHLRNumRstDtaSuccAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,17),_RuckusHLRNumRstDtaSuccAka_Type())
ruckusHLRNumRstDtaSuccAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumRstDtaSuccAka.setStatus(_A)
_RuckusHLRNumRstDtaFailErrHlrAka_Type=Counter64
_RuckusHLRNumRstDtaFailErrHlrAka_Object=MibTableColumn
ruckusHLRNumRstDtaFailErrHlrAka=_RuckusHLRNumRstDtaFailErrHlrAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,18),_RuckusHLRNumRstDtaFailErrHlrAka_Type())
ruckusHLRNumRstDtaFailErrHlrAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumRstDtaFailErrHlrAka.setStatus(_A)
_RuckusHLRNumRstDtaFailTmoAka_Type=Counter64
_RuckusHLRNumRstDtaFailTmoAka_Object=MibTableColumn
ruckusHLRNumRstDtaFailTmoAka=_RuckusHLRNumRstDtaFailTmoAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,19),_RuckusHLRNumRstDtaFailTmoAka_Type())
ruckusHLRNumRstDtaFailTmoAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumRstDtaFailTmoAka.setStatus(_A)
_RuckusHLRNumInsrtDtaSuccSim_Type=Counter64
_RuckusHLRNumInsrtDtaSuccSim_Object=MibTableColumn
ruckusHLRNumInsrtDtaSuccSim=_RuckusHLRNumInsrtDtaSuccSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,20),_RuckusHLRNumInsrtDtaSuccSim_Type())
ruckusHLRNumInsrtDtaSuccSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumInsrtDtaSuccSim.setStatus(_A)
_RuckusHLRNumInsrtDtaFailSim_Type=Counter64
_RuckusHLRNumInsrtDtaFailSim_Object=MibTableColumn
ruckusHLRNumInsrtDtaFailSim=_RuckusHLRNumInsrtDtaFailSim_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,21),_RuckusHLRNumInsrtDtaFailSim_Type())
ruckusHLRNumInsrtDtaFailSim.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumInsrtDtaFailSim.setStatus(_A)
_RuckusHLRNumInsrtDtaSuccAka_Type=Counter64
_RuckusHLRNumInsrtDtaSuccAka_Object=MibTableColumn
ruckusHLRNumInsrtDtaSuccAka=_RuckusHLRNumInsrtDtaSuccAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,22),_RuckusHLRNumInsrtDtaSuccAka_Type())
ruckusHLRNumInsrtDtaSuccAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumInsrtDtaSuccAka.setStatus(_A)
_RuckusHLRNumInsrtDtaFailAka_Type=Counter64
_RuckusHLRNumInsrtDtaFailAka_Object=MibTableColumn
ruckusHLRNumInsrtDtaFailAka=_RuckusHLRNumInsrtDtaFailAka_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,23),_RuckusHLRNumInsrtDtaFailAka_Type())
ruckusHLRNumInsrtDtaFailAka.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumInsrtDtaFailAka.setStatus(_A)
_RuckusHLRNumSaInsrtDtaSucc_Type=Counter64
_RuckusHLRNumSaInsrtDtaSucc_Object=MibTableColumn
ruckusHLRNumSaInsrtDtaSucc=_RuckusHLRNumSaInsrtDtaSucc_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,24),_RuckusHLRNumSaInsrtDtaSucc_Type())
ruckusHLRNumSaInsrtDtaSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumSaInsrtDtaSucc.setStatus(_A)
_RuckusHLRNumSaInsrtDtaFailUnkS_Type=Counter64
_RuckusHLRNumSaInsrtDtaFailUnkS_Object=MibTableColumn
ruckusHLRNumSaInsrtDtaFailUnkS=_RuckusHLRNumSaInsrtDtaFailUnkS_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,25),_RuckusHLRNumSaInsrtDtaFailUnkS_Type())
ruckusHLRNumSaInsrtDtaFailUnkS.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumSaInsrtDtaFailUnkS.setStatus(_A)
_RuckusHLRNumSaInsrtDtaFailErr_Type=Counter64
_RuckusHLRNumSaInsrtDtaFailErr_Object=MibTableColumn
ruckusHLRNumSaInsrtDtaFailErr=_RuckusHLRNumSaInsrtDtaFailErr_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,26),_RuckusHLRNumSaInsrtDtaFailErr_Type())
ruckusHLRNumSaInsrtDtaFailErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumSaInsrtDtaFailErr.setStatus(_A)
_RuckusHLRNumCfgAssoc_Type=Counter64
_RuckusHLRNumCfgAssoc_Object=MibTableColumn
ruckusHLRNumCfgAssoc=_RuckusHLRNumCfgAssoc_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,27),_RuckusHLRNumCfgAssoc_Type())
ruckusHLRNumCfgAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumCfgAssoc.setStatus(_A)
_RuckusHLRNumActAssoc_Type=Counter64
_RuckusHLRNumActAssoc_Object=MibTableColumn
ruckusHLRNumActAssoc=_RuckusHLRNumActAssoc_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,28),_RuckusHLRNumActAssoc_Type())
ruckusHLRNumActAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumActAssoc.setStatus(_A)
_RuckusHLRNumRtgFail_Type=Counter64
_RuckusHLRNumRtgFail_Object=MibTableColumn
ruckusHLRNumRtgFail=_RuckusHLRNumRtgFail_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,29),_RuckusHLRNumRtgFail_Type())
ruckusHLRNumRtgFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRNumRtgFail.setStatus(_A)
_RuckusHLRIndex_Type=Integer32
_RuckusHLRIndex_Object=MibTableColumn
ruckusHLRIndex=_RuckusHLRIndex_Object((1,3,6,1,4,1,25053,1,3,3,1,1,7,1,1,99),_RuckusHLRIndex_Type())
ruckusHLRIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusHLRIndex.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ruckusTTGMIB':ruckusTTGMIB,'ruckusTTGObjects':ruckusTTGObjects,'ruckusAAAInfo':ruckusAAAInfo,'ruckusAAATable':ruckusAAATable,'ruckusAAAEntry':ruckusAAAEntry,'ruckusAAAAaaIp':ruckusAAAAaaIp,'ruckusAAANumSuccAuthPerm':ruckusAAANumSuccAuthPerm,'ruckusAAANumFailAuthPerm':ruckusAAANumFailAuthPerm,'ruckusAAANumSuccAuthPsd':ruckusAAANumSuccAuthPsd,'ruckusAAANumFailAuthPsd':ruckusAAANumFailAuthPsd,'ruckusAAANumSuccFastAuth':ruckusAAANumSuccFastAuth,'ruckusAAANumFailFastAuth':ruckusAAANumFailFastAuth,'ruckusAAANumAuthUnknPsd':ruckusAAANumAuthUnknPsd,'ruckusAAANumAuthUnknFR':ruckusAAANumAuthUnknFR,'ruckusAAANumIncompleteAuth':ruckusAAANumIncompleteAuth,'ruckusAAANumSuccAcc':ruckusAAANumSuccAcc,'ruckusAAANumFailAcc':ruckusAAANumFailAcc,'ruckusAAANumRadAcsRq':ruckusAAANumRadAcsRq,'ruckusAAANumRadAcsAcpt':ruckusAAANumRadAcsAcpt,'ruckusAAANumRadAcsChlg':ruckusAAANumRadAcsChlg,'ruckusAAANumRadAcsRej':ruckusAAANumRadAcsRej,'ruckusAAANumRadAccRq':ruckusAAANumRadAccRq,'ruckusAAANumRadAccAcpt':ruckusAAANumRadAccAcpt,'ruckusAAANumRadCoaRq':ruckusAAANumRadCoaRq,'ruckusAAANumSuccCoaAcpt':ruckusAAANumSuccCoaAcpt,'ruckusAAANumFailCoaAcpt':ruckusAAANumFailCoaAcpt,'ruckusAAANumRadDmRq':ruckusAAANumRadDmRq,'ruckusAAANumSuccDmAcpt':ruckusAAANumSuccDmAcpt,'ruckusAAANumFailDmAcpt':ruckusAAANumFailDmAcpt,_D:ruckusAAAIndex,'ruckusAAAProxyInfo':ruckusAAAProxyInfo,'ruckusAAAProxyTable':ruckusAAAProxyTable,'ruckusAAAProxyEntry':ruckusAAAProxyEntry,'ruckusAAAProxyAaaIp':ruckusAAAProxyAaaIp,'ruckusAAAProxyNumSuccAuth':ruckusAAAProxyNumSuccAuth,'ruckusAAAProxyNumFailAuth':ruckusAAAProxyNumFailAuth,'ruckusAAAProxyNumIncmpltAuth':ruckusAAAProxyNumIncmpltAuth,'ruckusAAAProxyNumSuccAcc':ruckusAAAProxyNumSuccAcc,'ruckusAAAProxyNumFailAcc':ruckusAAAProxyNumFailAcc,'ruckusAAAProxyNumAcsRqRcvdNas':ruckusAAAProxyNumAcsRqRcvdNas,'ruckusAAAProxyNumAcsRqSntAaa':ruckusAAAProxyNumAcsRqSntAaa,'ruckusAAAProxyNumAcsChRcvdAaa':ruckusAAAProxyNumAcsChRcvdAaa,'ruckusAAAProxyNumAcsChSntNas':ruckusAAAProxyNumAcsChSntNas,'ruckusAAAProxyNumAcsAcpRcvdAaa':ruckusAAAProxyNumAcsAcpRcvdAaa,'ruckusAAAProxyNumAcsAcpSntNas':ruckusAAAProxyNumAcsAcpSntNas,'ruckusAAAProxyNumAcsRejRcvdAaa':ruckusAAAProxyNumAcsRejRcvdAaa,'ruckusAAAProxyNumAcsRejSntNas':ruckusAAAProxyNumAcsRejSntNas,'ruckusAAAProxyNumAccRqRcvdNas':ruckusAAAProxyNumAccRqRcvdNas,'ruckusAAAProxyNumAccRqSntAaa':ruckusAAAProxyNumAccRqSntAaa,'ruckusAAAProxyNumAccRspRcdAaa':ruckusAAAProxyNumAccRspRcdAaa,'ruckusAAAProxyNumAccRspSntNas':ruckusAAAProxyNumAccRspSntNas,'ruckusAAAProxyNumCoaRcvdAaa':ruckusAAAProxyNumCoaRcvdAaa,'ruckusAAAProxyNumCoaSucSntAaa':ruckusAAAProxyNumCoaSucSntAaa,'ruckusAAAProxyNumCoaFailSntAaa':ruckusAAAProxyNumCoaFailSntAaa,'ruckusAAAProxyNumDmRcvdAaa':ruckusAAAProxyNumDmRcvdAaa,'ruckusAAAProxyNumDmSntNas':ruckusAAAProxyNumDmSntNas,'ruckusAAAProxyNumDmSucRcdNas':ruckusAAAProxyNumDmSucRcdNas,'ruckusAAAProxyNumDmSucSntAaa':ruckusAAAProxyNumDmSucSntAaa,'ruckusAAAProxyNumDmFailRcdNas':ruckusAAAProxyNumDmFailRcdNas,'ruckusAAAProxyNumDmFailSntAaa':ruckusAAAProxyNumDmFailSntAaa,_E:ruckusAAAProxyIndex,'ruckusCGFInfo':ruckusCGFInfo,'ruckusCGFTable':ruckusCGFTable,'ruckusCGFEntry':ruckusCGFEntry,'ruckusCGFCgfSrvcName':ruckusCGFCgfSrvcName,'ruckusCGFCgfIp':ruckusCGFCgfIp,'ruckusCGFNumSuccCdrTxfd':ruckusCGFNumSuccCdrTxfd,'ruckusCGFNumCdrTxfrFail':ruckusCGFNumCdrTxfrFail,'ruckusCGFNumCdrPossDup':ruckusCGFNumCdrPossDup,'ruckusCGFNumCdrRlsReq':ruckusCGFNumCdrRlsReq,'ruckusCGFNumCdrCnclReq':ruckusCGFNumCdrCnclReq,'ruckusCGFNumDrtrReqSnt':ruckusCGFNumDrtrReqSnt,'ruckusCGFNumDrtrSucRspRcvd':ruckusCGFNumDrtrSucRspRcvd,'ruckusCGFNumDrtrFailRspRcvd':ruckusCGFNumDrtrFailRspRcvd,_F:ruckusCGFIndex,'ruckusGTPUInfo':ruckusGTPUInfo,'ruckusGTPUTable':ruckusGTPUTable,'ruckusGTPUEntry':ruckusGTPUEntry,'ruckusGTPUGgsnIPAddr':ruckusGTPUGgsnIPAddr,'ruckusGTPUTxPkts':ruckusGTPUTxPkts,'ruckusGTPUTxBytes':ruckusGTPUTxBytes,'ruckusGTPURxPkts':ruckusGTPURxPkts,'ruckusGTPURxBytes':ruckusGTPURxBytes,'ruckusGTPUTxDrops':ruckusGTPUTxDrops,'ruckusGTPURxDrops':ruckusGTPURxDrops,'ruckusGTPUNumBadGTPU':ruckusGTPUNumBadGTPU,'ruckusGTPUNumRXTeidInvalid':ruckusGTPUNumRXTeidInvalid,'ruckusGTPUNumTXTeidInvalid':ruckusGTPUNumTXTeidInvalid,'ruckusGTPUNumOfEchoRX':ruckusGTPUNumOfEchoRX,_G:ruckusGTPUIndex,'ruckusGGSNGTPCInfo':ruckusGGSNGTPCInfo,'ruckusGGSNGTPCTable':ruckusGGSNGTPCTable,'ruckusGGSNGTPCEntry':ruckusGGSNGTPCEntry,'ruckusGGSNGTPCGgsnIp':ruckusGGSNGTPCGgsnIp,'ruckusGGSNGTPCNumActPdp':ruckusGGSNGTPCNumActPdp,'ruckusGGSNGTPCSuccPdpCrt':ruckusGGSNGTPCSuccPdpCrt,'ruckusGGSNGTPCFailPdpCrt':ruckusGGSNGTPCFailPdpCrt,'ruckusGGSNGTPCSuccPdpUpdRcvd':ruckusGGSNGTPCSuccPdpUpdRcvd,'ruckusGGSNGTPCFailPdpUpdRcvd':ruckusGGSNGTPCFailPdpUpdRcvd,'ruckusGGSNGTPCSuccPdpUpdInitRM':ruckusGGSNGTPCSuccPdpUpdInitRM,'ruckusGGSNGTPCFailPdpUpdInitRM':ruckusGGSNGTPCFailPdpUpdInitRM,'ruckusGGSNGTPCSuccPdpUpdInitAAA':ruckusGGSNGTPCSuccPdpUpdInitAAA,'ruckusGGSNGTPCFailPdpUpdInitAAA':ruckusGGSNGTPCFailPdpUpdInitAAA,'ruckusGGSNGTPCSuccPdpUpdInitHLR':ruckusGGSNGTPCSuccPdpUpdInitHLR,'ruckusGGSNGTPCFailPdpUpdInitHLR':ruckusGGSNGTPCFailPdpUpdInitHLR,'ruckusGGSNGTPCSuccDelPdpRcvd':ruckusGGSNGTPCSuccDelPdpRcvd,'ruckusGGSNGTPCFailDelPdpRcvd':ruckusGGSNGTPCFailDelPdpRcvd,'ruckusGGSNGTPCSuccDelPdpInitErr':ruckusGGSNGTPCSuccDelPdpInitErr,'ruckusGGSNGTPCFailDelPdpInitErr':ruckusGGSNGTPCFailDelPdpInitErr,'ruckusGGSNGTPCSuccDelPdpInitDM':ruckusGGSNGTPCSuccDelPdpInitDM,'ruckusGGSNGTPCFailDelPdpInitDM':ruckusGGSNGTPCFailDelPdpInitDM,'ruckusGGSNGTPCSuccDelPdpInitHLR':ruckusGGSNGTPCSuccDelPdpInitHLR,'ruckusGGSNGTPCFailDelPdpInitHLR':ruckusGGSNGTPCFailDelPdpInitHLR,'ruckusGGSNGTPCSuccDelPdpInitSCG':ruckusGGSNGTPCSuccDelPdpInitSCG,'ruckusGGSNGTPCFailDelPdpInitSCG':ruckusGGSNGTPCFailDelPdpInitSCG,'ruckusGGSNGTPCSuccDelPdpInitAP':ruckusGGSNGTPCSuccDelPdpInitAP,'ruckusGGSNGTPCFailDelPdpInitAP':ruckusGGSNGTPCFailDelPdpInitAP,'ruckusGGSNGTPCSuccDelPdpInitD':ruckusGGSNGTPCSuccDelPdpInitD,'ruckusGGSNGTPCFailDelPdpInitD':ruckusGGSNGTPCFailDelPdpInitD,'ruckusGGSNGTPCSuccDelPdpInitClnt':ruckusGGSNGTPCSuccDelPdpInitClnt,'ruckusGGSNGTPCFailDelPdpInitClnt':ruckusGGSNGTPCFailDelPdpInitClnt,_H:ruckusGGSNGTPCIndex,'ruckusHLRInfo':ruckusHLRInfo,'ruckusHLRTable':ruckusHLRTable,'ruckusHLREntry':ruckusHLREntry,'ruckusHLRHlrSrvcName':ruckusHLRHlrSrvcName,'ruckusHLRNumSucAuthInfoReqSim':ruckusHLRNumSucAuthInfoReqSim,'ruckusHLRNumAuthInfoRqErrHlrSim':ruckusHLRNumAuthInfoRqErrHlrSim,'ruckusHLRNumAuthInfoRqTmotSim':ruckusHLRNumAuthInfoRqTmotSim,'ruckusHLRNumSucAuthInfoReqAka':ruckusHLRNumSucAuthInfoReqAka,'ruckusHLRNumAuthInfoRqErrHlrAka':ruckusHLRNumAuthInfoRqErrHlrAka,'ruckusHLRNumAuthInfoRqTmotAka':ruckusHLRNumAuthInfoRqTmotAka,'ruckusHLRNumUpdGprsSuccSim':ruckusHLRNumUpdGprsSuccSim,'ruckusHLRNumUpdGprsFailErrSim':ruckusHLRNumUpdGprsFailErrSim,'ruckusHLRNumUpdGprsFailTmoSim':ruckusHLRNumUpdGprsFailTmoSim,'ruckusHLRNumUpdGprsSuccAka':ruckusHLRNumUpdGprsSuccAka,'ruckusHLRNumUpdGprsFailErrAka':ruckusHLRNumUpdGprsFailErrAka,'ruckusHLRNumUpdGprsFailTmoAka':ruckusHLRNumUpdGprsFailTmoAka,'ruckusHLRNumRstDtaSuccSim':ruckusHLRNumRstDtaSuccSim,'ruckusHLRNumRstDtaFailErrHlrSim':ruckusHLRNumRstDtaFailErrHlrSim,'ruckusHLRNumRstDtaFailTmoSim':ruckusHLRNumRstDtaFailTmoSim,'ruckusHLRNumRstDtaSuccAka':ruckusHLRNumRstDtaSuccAka,'ruckusHLRNumRstDtaFailErrHlrAka':ruckusHLRNumRstDtaFailErrHlrAka,'ruckusHLRNumRstDtaFailTmoAka':ruckusHLRNumRstDtaFailTmoAka,'ruckusHLRNumInsrtDtaSuccSim':ruckusHLRNumInsrtDtaSuccSim,'ruckusHLRNumInsrtDtaFailSim':ruckusHLRNumInsrtDtaFailSim,'ruckusHLRNumInsrtDtaSuccAka':ruckusHLRNumInsrtDtaSuccAka,'ruckusHLRNumInsrtDtaFailAka':ruckusHLRNumInsrtDtaFailAka,'ruckusHLRNumSaInsrtDtaSucc':ruckusHLRNumSaInsrtDtaSucc,'ruckusHLRNumSaInsrtDtaFailUnkS':ruckusHLRNumSaInsrtDtaFailUnkS,'ruckusHLRNumSaInsrtDtaFailErr':ruckusHLRNumSaInsrtDtaFailErr,'ruckusHLRNumCfgAssoc':ruckusHLRNumCfgAssoc,'ruckusHLRNumActAssoc':ruckusHLRNumActAssoc,'ruckusHLRNumRtgFail':ruckusHLRNumRtgFail,_I:ruckusHLRIndex})