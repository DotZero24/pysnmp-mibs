_H='nsIpArpIndex'
_G='NETSCREEN-IP-ARP-MIB'
_F='not-accessible'
_E='enabled'
_D='disable'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenIp,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenIp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nsIpArp=ModuleIdentity((1,3,6,1,4,1,3224,17,1))
if mibBuilder.loadTexts:nsIpArp.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-02 00:00'))
class _NsIpArpAOD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIpArpAOD_Type.__name__=_C
_NsIpArpAOD_Object=MibScalar
nsIpArpAOD=_NsIpArpAOD_Object((1,3,6,1,4,1,3224,17,1,1),_NsIpArpAOD_Type())
nsIpArpAOD.setMaxAccess(_F)
if mibBuilder.loadTexts:nsIpArpAOD.setStatus(_A)
class _NsIpArpCachUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsIpArpCachUpdate_Type.__name__=_C
_NsIpArpCachUpdate_Object=MibScalar
nsIpArpCachUpdate=_NsIpArpCachUpdate_Object((1,3,6,1,4,1,3224,17,1,2),_NsIpArpCachUpdate_Type())
nsIpArpCachUpdate.setMaxAccess(_F)
if mibBuilder.loadTexts:nsIpArpCachUpdate.setStatus(_A)
_NsIpArpTable_Object=MibTable
nsIpArpTable=_NsIpArpTable_Object((1,3,6,1,4,1,3224,17,1,3))
if mibBuilder.loadTexts:nsIpArpTable.setStatus(_A)
_NsIpArpEntry_Object=MibTableRow
nsIpArpEntry=_NsIpArpEntry_Object((1,3,6,1,4,1,3224,17,1,3,1))
nsIpArpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:nsIpArpEntry.setStatus(_A)
class _NsIpArpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsIpArpIndex_Type.__name__=_C
_NsIpArpIndex_Object=MibTableColumn
nsIpArpIndex=_NsIpArpIndex_Object((1,3,6,1,4,1,3224,17,1,3,1,1),_NsIpArpIndex_Type())
nsIpArpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpIndex.setStatus(_A)
_NsIpArpIp_Type=IpAddress
_NsIpArpIp_Object=MibTableColumn
nsIpArpIp=_NsIpArpIp_Object((1,3,6,1,4,1,3224,17,1,3,1,2),_NsIpArpIp_Type())
nsIpArpIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpIp.setStatus(_A)
_NsIpArpMac_Type=PhysAddress
_NsIpArpMac_Object=MibTableColumn
nsIpArpMac=_NsIpArpMac_Object((1,3,6,1,4,1,3224,17,1,3,1,3),_NsIpArpMac_Type())
nsIpArpMac.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpMac.setStatus(_A)
_NsIpArpVsys_Type=Integer32
_NsIpArpVsys_Object=MibTableColumn
nsIpArpVsys=_NsIpArpVsys_Object((1,3,6,1,4,1,3224,17,1,3,1,4),_NsIpArpVsys_Type())
nsIpArpVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpVsys.setStatus(_A)
_NsIpArpIfIdx_Type=Integer32
_NsIpArpIfIdx_Object=MibTableColumn
nsIpArpIfIdx=_NsIpArpIfIdx_Object((1,3,6,1,4,1,3224,17,1,3,1,5),_NsIpArpIfIdx_Type())
nsIpArpIfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpIfIdx.setStatus(_A)
class _NsIpArpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pending',1),('valid',2),('delete',3),('static',4)))
_NsIpArpState_Type.__name__=_C
_NsIpArpState_Object=MibTableColumn
nsIpArpState=_NsIpArpState_Object((1,3,6,1,4,1,3224,17,1,3,1,6),_NsIpArpState_Type())
nsIpArpState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpState.setStatus(_A)
_NsIpArpAge_Type=Integer32
_NsIpArpAge_Object=MibTableColumn
nsIpArpAge=_NsIpArpAge_Object((1,3,6,1,4,1,3224,17,1,3,1,7),_NsIpArpAge_Type())
nsIpArpAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpAge.setStatus(_A)
_NsIpArpRetry_Type=Integer32
_NsIpArpRetry_Object=MibTableColumn
nsIpArpRetry=_NsIpArpRetry_Object((1,3,6,1,4,1,3224,17,1,3,1,8),_NsIpArpRetry_Type())
nsIpArpRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpRetry.setStatus(_A)
_NsIpArpPakQue_Type=Integer32
_NsIpArpPakQue_Object=MibTableColumn
nsIpArpPakQue=_NsIpArpPakQue_Object((1,3,6,1,4,1,3224,17,1,3,1,9),_NsIpArpPakQue_Type())
nsIpArpPakQue.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIpArpPakQue.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'nsIpArp':nsIpArp,'nsIpArpAOD':nsIpArpAOD,'nsIpArpCachUpdate':nsIpArpCachUpdate,'nsIpArpTable':nsIpArpTable,'nsIpArpEntry':nsIpArpEntry,_H:nsIpArpIndex,'nsIpArpIp':nsIpArpIp,'nsIpArpMac':nsIpArpMac,'nsIpArpVsys':nsIpArpVsys,'nsIpArpIfIdx':nsIpArpIfIdx,'nsIpArpState':nsIpArpState,'nsIpArpAge':nsIpArpAge,'nsIpArpRetry':nsIpArpRetry,'nsIpArpPakQue':nsIpArpPakQue})