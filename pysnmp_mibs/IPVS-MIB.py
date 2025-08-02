_G='totRSIdx'
_F='not-accessible'
_E='IPVS-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
one4net,=mibBuilder.importSymbols('ONE4NET-MIB','one4net')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipvs=ModuleIdentity((1,3,6,1,4,1,12196,12))
if mibBuilder.loadTexts:ipvs.setRevisions(('2021-06-25 09:06',))
_IpvsVSTable_Object=MibTable
ipvsVSTable=_IpvsVSTable_Object((1,3,6,1,4,1,12196,12,1))
if mibBuilder.loadTexts:ipvsVSTable.setStatus(_A)
_VsEntry_Object=MibTableRow
vsEntry=_VsEntry_Object((1,3,6,1,4,1,12196,12,1,1))
vsEntry.setIndexNames((0,_E,'vSIdx'))
if mibBuilder.loadTexts:vsEntry.setStatus(_A)
class _VSIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_VSIdx_Type.__name__=_C
_VSIdx_Object=MibTableColumn
vSIdx=_VSIdx_Object((1,3,6,1,4,1,12196,12,1,1,1),_VSIdx_Type())
vSIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:vSIdx.setStatus(_A)
class _VSDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_VSDesc_Type.__name__=_D
_VSDesc_Object=MibTableColumn
vSDesc=_VSDesc_Object((1,3,6,1,4,1,12196,12,1,1,11),_VSDesc_Type())
vSDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:vSDesc.setStatus(_A)
_VSConns_Type=Counter32
_VSConns_Object=MibTableColumn
vSConns=_VSConns_Object((1,3,6,1,4,1,12196,12,1,1,12),_VSConns_Type())
vSConns.setMaxAccess(_B)
if mibBuilder.loadTexts:vSConns.setStatus(_A)
_VSInPkts_Type=Counter32
_VSInPkts_Object=MibTableColumn
vSInPkts=_VSInPkts_Object((1,3,6,1,4,1,12196,12,1,1,13),_VSInPkts_Type())
vSInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vSInPkts.setStatus(_A)
_VSOutPkts_Type=Counter32
_VSOutPkts_Object=MibTableColumn
vSOutPkts=_VSOutPkts_Object((1,3,6,1,4,1,12196,12,1,1,14),_VSOutPkts_Type())
vSOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vSOutPkts.setStatus(_A)
_VSInBytes_Type=Counter64
_VSInBytes_Object=MibTableColumn
vSInBytes=_VSInBytes_Object((1,3,6,1,4,1,12196,12,1,1,15),_VSInBytes_Type())
vSInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vSInBytes.setStatus(_A)
_VSOutBytes_Type=Counter64
_VSOutBytes_Object=MibTableColumn
vSOutBytes=_VSOutBytes_Object((1,3,6,1,4,1,12196,12,1,1,16),_VSOutBytes_Type())
vSOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vSOutBytes.setStatus(_A)
_VSActiveConns_Type=Gauge32
_VSActiveConns_Object=MibTableColumn
vSActiveConns=_VSActiveConns_Object((1,3,6,1,4,1,12196,12,1,1,17),_VSActiveConns_Type())
vSActiveConns.setMaxAccess(_B)
if mibBuilder.loadTexts:vSActiveConns.setStatus(_A)
_IpvsRSTable_Object=MibTable
ipvsRSTable=_IpvsRSTable_Object((1,3,6,1,4,1,12196,12,2))
if mibBuilder.loadTexts:ipvsRSTable.setStatus(_A)
_RsEntry_Object=MibTableRow
rsEntry=_RsEntry_Object((1,3,6,1,4,1,12196,12,2,1))
rsEntry.setIndexNames((0,_E,'rSIdx'))
if mibBuilder.loadTexts:rsEntry.setStatus(_A)
class _RSIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_RSIdx_Type.__name__=_C
_RSIdx_Object=MibTableColumn
rSIdx=_RSIdx_Object((1,3,6,1,4,1,12196,12,2,1,1),_RSIdx_Type())
rSIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:rSIdx.setStatus(_A)
class _RSVSidx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RSVSidx_Type.__name__=_C
_RSVSidx_Object=MibTableColumn
rSVSidx=_RSVSidx_Object((1,3,6,1,4,1,12196,12,2,1,2),_RSVSidx_Type())
rSVSidx.setMaxAccess(_B)
if mibBuilder.loadTexts:rSVSidx.setStatus(_A)
class _RSDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8192))
_RSDesc_Type.__name__=_D
_RSDesc_Object=MibTableColumn
rSDesc=_RSDesc_Object((1,3,6,1,4,1,12196,12,2,1,11),_RSDesc_Type())
rSDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rSDesc.setStatus(_A)
_RSConns_Type=Counter32
_RSConns_Object=MibTableColumn
rSConns=_RSConns_Object((1,3,6,1,4,1,12196,12,2,1,12),_RSConns_Type())
rSConns.setMaxAccess(_B)
if mibBuilder.loadTexts:rSConns.setStatus(_A)
_RSInPkts_Type=Counter32
_RSInPkts_Object=MibTableColumn
rSInPkts=_RSInPkts_Object((1,3,6,1,4,1,12196,12,2,1,13),_RSInPkts_Type())
rSInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rSInPkts.setStatus(_A)
_RSOutPkts_Type=Counter32
_RSOutPkts_Object=MibTableColumn
rSOutPkts=_RSOutPkts_Object((1,3,6,1,4,1,12196,12,2,1,14),_RSOutPkts_Type())
rSOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rSOutPkts.setStatus(_A)
_RSInBytes_Type=Counter64
_RSInBytes_Object=MibTableColumn
rSInBytes=_RSInBytes_Object((1,3,6,1,4,1,12196,12,2,1,15),_RSInBytes_Type())
rSInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rSInBytes.setStatus(_A)
_RSOutBytes_Type=Counter64
_RSOutBytes_Object=MibTableColumn
rSOutBytes=_RSOutBytes_Object((1,3,6,1,4,1,12196,12,2,1,16),_RSOutBytes_Type())
rSOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rSOutBytes.setStatus(_A)
_RSActiveConns_Type=Gauge32
_RSActiveConns_Object=MibTableColumn
rSActiveConns=_RSActiveConns_Object((1,3,6,1,4,1,12196,12,2,1,17),_RSActiveConns_Type())
rSActiveConns.setMaxAccess(_B)
if mibBuilder.loadTexts:rSActiveConns.setStatus(_A)
_RSInactiveConns_Type=Counter32
_RSInactiveConns_Object=MibTableColumn
rSInactiveConns=_RSInactiveConns_Object((1,3,6,1,4,1,12196,12,2,1,18),_RSInactiveConns_Type())
rSInactiveConns.setMaxAccess(_B)
if mibBuilder.loadTexts:rSInactiveConns.setStatus(_A)
_RSWeight_Type=Integer32
_RSWeight_Object=MibTableColumn
rSWeight=_RSWeight_Object((1,3,6,1,4,1,12196,12,2,1,19),_RSWeight_Type())
rSWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:rSWeight.setStatus(_A)
_Conns_Type=Counter32
_Conns_Object=MibScalar
conns=_Conns_Object((1,3,6,1,4,1,12196,12,3),_Conns_Type())
conns.setMaxAccess(_B)
if mibBuilder.loadTexts:conns.setStatus(_A)
_InPkts_Type=Counter32
_InPkts_Object=MibScalar
inPkts=_InPkts_Object((1,3,6,1,4,1,12196,12,4),_InPkts_Type())
inPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:inPkts.setStatus(_A)
_OutPkts_Type=Counter32
_OutPkts_Object=MibScalar
outPkts=_OutPkts_Object((1,3,6,1,4,1,12196,12,5),_OutPkts_Type())
outPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:outPkts.setStatus(_A)
_InBytes_Type=Counter64
_InBytes_Object=MibScalar
inBytes=_InBytes_Object((1,3,6,1,4,1,12196,12,6),_InBytes_Type())
inBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:inBytes.setStatus(_A)
_OutBytes_Type=Counter64
_OutBytes_Object=MibScalar
outBytes=_OutBytes_Object((1,3,6,1,4,1,12196,12,7),_OutBytes_Type())
outBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:outBytes.setStatus(_A)
_IpvsRSTotalTable_Object=MibTable
ipvsRSTotalTable=_IpvsRSTotalTable_Object((1,3,6,1,4,1,12196,12,8))
if mibBuilder.loadTexts:ipvsRSTotalTable.setStatus(_A)
_RsTotalEntry_Object=MibTableRow
rsTotalEntry=_RsTotalEntry_Object((1,3,6,1,4,1,12196,12,8,1))
rsTotalEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:rsTotalEntry.setStatus(_A)
class _TotRSIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_TotRSIdx_Type.__name__=_C
_TotRSIdx_Object=MibTableColumn
totRSIdx=_TotRSIdx_Object((1,3,6,1,4,1,12196,12,8,1,1),_TotRSIdx_Type())
totRSIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSIdx.setStatus(_A)
class _TotRSDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8192))
_TotRSDesc_Type.__name__=_D
_TotRSDesc_Object=MibTableColumn
totRSDesc=_TotRSDesc_Object((1,3,6,1,4,1,12196,12,8,1,2),_TotRSDesc_Type())
totRSDesc.setMaxAccess(_F)
if mibBuilder.loadTexts:totRSDesc.setStatus(_A)
_TotRSConns_Type=Counter32
_TotRSConns_Object=MibTableColumn
totRSConns=_TotRSConns_Object((1,3,6,1,4,1,12196,12,8,1,3),_TotRSConns_Type())
totRSConns.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSConns.setStatus(_A)
_TotRSInPkts_Type=Counter32
_TotRSInPkts_Object=MibTableColumn
totRSInPkts=_TotRSInPkts_Object((1,3,6,1,4,1,12196,12,8,1,4),_TotRSInPkts_Type())
totRSInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSInPkts.setStatus(_A)
_TotRSOutPkts_Type=Counter32
_TotRSOutPkts_Object=MibTableColumn
totRSOutPkts=_TotRSOutPkts_Object((1,3,6,1,4,1,12196,12,8,1,5),_TotRSOutPkts_Type())
totRSOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSOutPkts.setStatus(_A)
_TotRSInBytes_Type=Counter64
_TotRSInBytes_Object=MibTableColumn
totRSInBytes=_TotRSInBytes_Object((1,3,6,1,4,1,12196,12,8,1,6),_TotRSInBytes_Type())
totRSInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSInBytes.setStatus(_A)
_TotRSOutBytes_Type=Counter64
_TotRSOutBytes_Object=MibTableColumn
totRSOutBytes=_TotRSOutBytes_Object((1,3,6,1,4,1,12196,12,8,1,7),_TotRSOutBytes_Type())
totRSOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSOutBytes.setStatus(_A)
_TotRSActiveConns_Type=Gauge32
_TotRSActiveConns_Object=MibTableColumn
totRSActiveConns=_TotRSActiveConns_Object((1,3,6,1,4,1,12196,12,8,1,8),_TotRSActiveConns_Type())
totRSActiveConns.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSActiveConns.setStatus(_A)
_TotRSInactiveConns_Type=Counter32
_TotRSInactiveConns_Object=MibTableColumn
totRSInactiveConns=_TotRSInactiveConns_Object((1,3,6,1,4,1,12196,12,8,1,9),_TotRSInactiveConns_Type())
totRSInactiveConns.setMaxAccess(_B)
if mibBuilder.loadTexts:totRSInactiveConns.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ipvs':ipvs,'ipvsVSTable':ipvsVSTable,'vsEntry':vsEntry,'vSIdx':vSIdx,'vSDesc':vSDesc,'vSConns':vSConns,'vSInPkts':vSInPkts,'vSOutPkts':vSOutPkts,'vSInBytes':vSInBytes,'vSOutBytes':vSOutBytes,'vSActiveConns':vSActiveConns,'ipvsRSTable':ipvsRSTable,'rsEntry':rsEntry,'rSIdx':rSIdx,'rSVSidx':rSVSidx,'rSDesc':rSDesc,'rSConns':rSConns,'rSInPkts':rSInPkts,'rSOutPkts':rSOutPkts,'rSInBytes':rSInBytes,'rSOutBytes':rSOutBytes,'rSActiveConns':rSActiveConns,'rSInactiveConns':rSInactiveConns,'rSWeight':rSWeight,'conns':conns,'inPkts':inPkts,'outPkts':outPkts,'inBytes':inBytes,'outBytes':outBytes,'ipvsRSTotalTable':ipvsRSTotalTable,'rsTotalEntry':rsTotalEntry,_G:totRSIdx,'totRSDesc':totRSDesc,'totRSConns':totRSConns,'totRSInPkts':totRSInPkts,'totRSOutPkts':totRSOutPkts,'totRSInBytes':totRSInBytes,'totRSOutBytes':totRSOutBytes,'totRSActiveConns':totRSActiveConns,'totRSInactiveConns':totRSInactiveConns})