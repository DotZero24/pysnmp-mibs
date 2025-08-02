_M='upnpIfIndex'
_L='ipNatUPnPExtPort'
_K='ipNatUPnPRemoteAddr'
_J='ipNatUPnPProtocol'
_I='ipNatUPnPIfIndex'
_H='DisplayString'
_G='disabled'
_F='enabled'
_E='BIANCA-BRICK-UPNP-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_Upnp_ObjectIdentity=ObjectIdentity
upnp=_Upnp_ObjectIdentity((1,3,6,1,4,1,272,4,5,45))
_UpnpGlobals_ObjectIdentity=ObjectIdentity
upnpGlobals=_UpnpGlobals_ObjectIdentity((1,3,6,1,4,1,272,4,5,45,10))
class _UpnpGlobStatus_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30)));namedValues=NamedValues(*((_F,10),('restricted',20),(_G,30)))
_UpnpGlobStatus_Type.__name__=_B
_UpnpGlobStatus_Object=MibScalar
upnpGlobStatus=_UpnpGlobStatus_Object((1,3,6,1,4,1,272,4,5,45,10,10),_UpnpGlobStatus_Type())
upnpGlobStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upnpGlobStatus.setStatus(_A)
class _UpnpGlobTcpPort_Type(Integer32):defaultValue=5678;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UpnpGlobTcpPort_Type.__name__=_B
_UpnpGlobTcpPort_Object=MibScalar
upnpGlobTcpPort=_UpnpGlobTcpPort_Object((1,3,6,1,4,1,272,4,5,45,10,20),_UpnpGlobTcpPort_Type())
upnpGlobTcpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:upnpGlobTcpPort.setStatus(_A)
class _UpnpGlobSsdpTtl_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_UpnpGlobSsdpTtl_Type.__name__=_B
_UpnpGlobSsdpTtl_Object=MibScalar
upnpGlobSsdpTtl=_UpnpGlobSsdpTtl_Object((1,3,6,1,4,1,272,4,5,45,10,30),_UpnpGlobSsdpTtl_Type())
upnpGlobSsdpTtl.setMaxAccess(_D)
if mibBuilder.loadTexts:upnpGlobSsdpTtl.setStatus(_A)
_IpNatUPnPTable_Object=MibTable
ipNatUPnPTable=_IpNatUPnPTable_Object((1,3,6,1,4,1,272,4,5,45,20))
if mibBuilder.loadTexts:ipNatUPnPTable.setStatus(_A)
_IpNatUPnPEntry_Object=MibTableRow
ipNatUPnPEntry=_IpNatUPnPEntry_Object((1,3,6,1,4,1,272,4,5,45,20,10))
ipNatUPnPEntry.setIndexNames((0,_E,_I),(0,_E,_J),(0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:ipNatUPnPEntry.setStatus(_A)
_IpNatUPnPIfIndex_Type=Integer32
_IpNatUPnPIfIndex_Object=MibTableColumn
ipNatUPnPIfIndex=_IpNatUPnPIfIndex_Object((1,3,6,1,4,1,272,4,5,45,20,10,10),_IpNatUPnPIfIndex_Type())
ipNatUPnPIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPIfIndex.setStatus(_A)
class _IpNatUPnPProtocol_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17)));namedValues=NamedValues(*(('tcp',6),('udp',17)))
_IpNatUPnPProtocol_Type.__name__=_B
_IpNatUPnPProtocol_Object=MibTableColumn
ipNatUPnPProtocol=_IpNatUPnPProtocol_Object((1,3,6,1,4,1,272,4,5,45,20,10,20),_IpNatUPnPProtocol_Type())
ipNatUPnPProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPProtocol.setStatus(_A)
_IpNatUPnPRemoteAddr_Type=IpAddress
_IpNatUPnPRemoteAddr_Object=MibTableColumn
ipNatUPnPRemoteAddr=_IpNatUPnPRemoteAddr_Object((1,3,6,1,4,1,272,4,5,45,20,10,30),_IpNatUPnPRemoteAddr_Type())
ipNatUPnPRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPRemoteAddr.setStatus(_A)
class _IpNatUPnPExtPort_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_IpNatUPnPExtPort_Type.__name__=_B
_IpNatUPnPExtPort_Object=MibTableColumn
ipNatUPnPExtPort=_IpNatUPnPExtPort_Object((1,3,6,1,4,1,272,4,5,45,20,10,40),_IpNatUPnPExtPort_Type())
ipNatUPnPExtPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPExtPort.setStatus(_A)
_IpNatUPnPIntAddr_Type=IpAddress
_IpNatUPnPIntAddr_Object=MibTableColumn
ipNatUPnPIntAddr=_IpNatUPnPIntAddr_Object((1,3,6,1,4,1,272,4,5,45,20,10,50),_IpNatUPnPIntAddr_Type())
ipNatUPnPIntAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPIntAddr.setStatus(_A)
class _IpNatUPnPIntPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpNatUPnPIntPort_Type.__name__=_B
_IpNatUPnPIntPort_Object=MibTableColumn
ipNatUPnPIntPort=_IpNatUPnPIntPort_Object((1,3,6,1,4,1,272,4,5,45,20,10,60),_IpNatUPnPIntPort_Type())
ipNatUPnPIntPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPIntPort.setStatus(_A)
class _IpNatUPnPLeaseDuration_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5184000))
_IpNatUPnPLeaseDuration_Type.__name__=_B
_IpNatUPnPLeaseDuration_Object=MibTableColumn
ipNatUPnPLeaseDuration=_IpNatUPnPLeaseDuration_Object((1,3,6,1,4,1,272,4,5,45,20,10,70),_IpNatUPnPLeaseDuration_Type())
ipNatUPnPLeaseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPLeaseDuration.setStatus(_A)
class _IpNatUPnPStatus_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30)));namedValues=NamedValues(*(('delete',10),(_F,20),(_G,30)))
_IpNatUPnPStatus_Type.__name__=_B
_IpNatUPnPStatus_Object=MibTableColumn
ipNatUPnPStatus=_IpNatUPnPStatus_Object((1,3,6,1,4,1,272,4,5,45,20,10,80),_IpNatUPnPStatus_Type())
ipNatUPnPStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipNatUPnPStatus.setStatus(_A)
class _IpNatUPnPDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpNatUPnPDescription_Type.__name__=_H
_IpNatUPnPDescription_Object=MibTableColumn
ipNatUPnPDescription=_IpNatUPnPDescription_Object((1,3,6,1,4,1,272,4,5,45,20,10,90),_IpNatUPnPDescription_Type())
ipNatUPnPDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNatUPnPDescription.setStatus(_A)
_UpnpIfTable_Object=MibTable
upnpIfTable=_UpnpIfTable_Object((1,3,6,1,4,1,272,4,5,45,30))
if mibBuilder.loadTexts:upnpIfTable.setStatus(_A)
_UpnpIfEntry_Object=MibTableRow
upnpIfEntry=_UpnpIfEntry_Object((1,3,6,1,4,1,272,4,5,45,30,10))
upnpIfEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:upnpIfEntry.setStatus(_A)
_UpnpIfIndex_Type=Integer32
_UpnpIfIndex_Object=MibTableColumn
upnpIfIndex=_UpnpIfIndex_Object((1,3,6,1,4,1,272,4,5,45,30,10,10),_UpnpIfIndex_Type())
upnpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:upnpIfIndex.setStatus(_A)
class _UpnpIfClientRequests_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20)));namedValues=NamedValues(*((_F,10),(_G,20)))
_UpnpIfClientRequests_Type.__name__=_B
_UpnpIfClientRequests_Object=MibTableColumn
upnpIfClientRequests=_UpnpIfClientRequests_Object((1,3,6,1,4,1,272,4,5,45,30,10,20),_UpnpIfClientRequests_Type())
upnpIfClientRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:upnpIfClientRequests.setStatus(_A)
class _UpnpIfUPnPControlled_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20)));namedValues=NamedValues(*((_F,10),(_G,20)))
_UpnpIfUPnPControlled_Type.__name__=_B
_UpnpIfUPnPControlled_Object=MibTableColumn
upnpIfUPnPControlled=_UpnpIfUPnPControlled_Object((1,3,6,1,4,1,272,4,5,45,30,10,30),_UpnpIfUPnPControlled_Type())
upnpIfUPnPControlled.setMaxAccess(_D)
if mibBuilder.loadTexts:upnpIfUPnPControlled.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'upnp':upnp,'upnpGlobals':upnpGlobals,'upnpGlobStatus':upnpGlobStatus,'upnpGlobTcpPort':upnpGlobTcpPort,'upnpGlobSsdpTtl':upnpGlobSsdpTtl,'ipNatUPnPTable':ipNatUPnPTable,'ipNatUPnPEntry':ipNatUPnPEntry,_I:ipNatUPnPIfIndex,_J:ipNatUPnPProtocol,_K:ipNatUPnPRemoteAddr,_L:ipNatUPnPExtPort,'ipNatUPnPIntAddr':ipNatUPnPIntAddr,'ipNatUPnPIntPort':ipNatUPnPIntPort,'ipNatUPnPLeaseDuration':ipNatUPnPLeaseDuration,'ipNatUPnPStatus':ipNatUPnPStatus,'ipNatUPnPDescription':ipNatUPnPDescription,'upnpIfTable':upnpIfTable,'upnpIfEntry':upnpIfEntry,_M:upnpIfIndex,'upnpIfClientRequests':upnpIfClientRequests,'upnpIfUPnPControlled':upnpIfUPnPControlled})