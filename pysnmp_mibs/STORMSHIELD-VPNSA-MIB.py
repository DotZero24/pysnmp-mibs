_E='snsVPNSAIndex'
_D='STORMSHIELD-VPNSA-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsVPN=ModuleIdentity((1,3,6,1,4,1,11256,1,1))
if mibBuilder.loadTexts:snsVPN.setRevisions(('2017-02-20 00:00',))
_SnsVPNSATable_Object=MibTable
snsVPNSATable=_SnsVPNSATable_Object((1,3,6,1,4,1,11256,1,1,1))
if mibBuilder.loadTexts:snsVPNSATable.setStatus(_A)
_SnsVPNSAEntry_Object=MibTableRow
snsVPNSAEntry=_SnsVPNSAEntry_Object((1,3,6,1,4,1,11256,1,1,1,1))
snsVPNSAEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsVPNSAEntry.setStatus(_A)
class _SnsVPNSAIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnsVPNSAIndex_Type.__name__=_C
_SnsVPNSAIndex_Object=MibTableColumn
snsVPNSAIndex=_SnsVPNSAIndex_Object((1,3,6,1,4,1,11256,1,1,1,1,1),_SnsVPNSAIndex_Type())
snsVPNSAIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNSAIndex.setStatus(_A)
_SnsVPNIPSrc_Type=DisplayString
_SnsVPNIPSrc_Object=MibTableColumn
snsVPNIPSrc=_SnsVPNIPSrc_Object((1,3,6,1,4,1,11256,1,1,1,1,2),_SnsVPNIPSrc_Type())
snsVPNIPSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNIPSrc.setStatus(_A)
_SnsVPNIPDst_Type=DisplayString
_SnsVPNIPDst_Object=MibTableColumn
snsVPNIPDst=_SnsVPNIPDst_Object((1,3,6,1,4,1,11256,1,1,1,1,3),_SnsVPNIPDst_Type())
snsVPNIPDst.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNIPDst.setStatus(_A)
class _SnsVPNType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unspec',0),('unknown',1),('ah',2),('esp',3),('rsvp',4),('ospfv2',5),('ripv2',6),('mip',7),('ipcomp',8)))
_SnsVPNType_Type.__name__=_C
_SnsVPNType_Object=MibTableColumn
snsVPNType=_SnsVPNType_Object((1,3,6,1,4,1,11256,1,1,1,1,4),_SnsVPNType_Type())
snsVPNType.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNType.setStatus(_A)
class _SnsVPNMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('any',0),('transport',1),('tunnel',2)))
_SnsVPNMode_Type.__name__=_C
_SnsVPNMode_Object=MibTableColumn
snsVPNMode=_SnsVPNMode_Object((1,3,6,1,4,1,11256,1,1,1,1,5),_SnsVPNMode_Type())
snsVPNMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNMode.setStatus(_A)
_SnsVPNSpi_Type=Unsigned32
_SnsVPNSpi_Object=MibTableColumn
snsVPNSpi=_SnsVPNSpi_Object((1,3,6,1,4,1,11256,1,1,1,1,6),_SnsVPNSpi_Type())
snsVPNSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNSpi.setStatus(_A)
_SnsVPNPeerSpi_Type=Unsigned32
_SnsVPNPeerSpi_Object=MibTableColumn
snsVPNPeerSpi=_SnsVPNPeerSpi_Object((1,3,6,1,4,1,11256,1,1,1,1,7),_SnsVPNPeerSpi_Type())
snsVPNPeerSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNPeerSpi.setStatus(_A)
_SnsVPNReqID_Type=Integer32
_SnsVPNReqID_Object=MibTableColumn
snsVPNReqID=_SnsVPNReqID_Object((1,3,6,1,4,1,11256,1,1,1,1,8),_SnsVPNReqID_Type())
snsVPNReqID.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNReqID.setStatus(_A)
_SnsVPNEnc_Type=DisplayString
_SnsVPNEnc_Object=MibTableColumn
snsVPNEnc=_SnsVPNEnc_Object((1,3,6,1,4,1,11256,1,1,1,1,9),_SnsVPNEnc_Type())
snsVPNEnc.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNEnc.setStatus(_A)
class _SnsVPNAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,5,6,7,249,250,251)));namedValues=NamedValues(*(('none',0),('hmac-md5',2),('hmac-sha1',3),('hmac-sha256',5),('hmac-sha384',6),('hmac-sha512',7),('md5',249),('sha',250),('null',251)))
_SnsVPNAuth_Type.__name__=_C
_SnsVPNAuth_Object=MibTableColumn
snsVPNAuth=_SnsVPNAuth_Object((1,3,6,1,4,1,11256,1,1,1,1,10),_SnsVPNAuth_Type())
snsVPNAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNAuth.setStatus(_A)
class _SnsVPNState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('larval',0),('mature',1),('dying',2),('dead',3)))
_SnsVPNState_Type.__name__=_C
_SnsVPNState_Object=MibTableColumn
snsVPNState=_SnsVPNState_Object((1,3,6,1,4,1,11256,1,1,1,1,11),_SnsVPNState_Type())
snsVPNState.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNState.setStatus(_A)
_SnsVPNLifetime_Type=Counter64
_SnsVPNLifetime_Object=MibTableColumn
snsVPNLifetime=_SnsVPNLifetime_Object((1,3,6,1,4,1,11256,1,1,1,1,12),_SnsVPNLifetime_Type())
snsVPNLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNLifetime.setStatus(_A)
_SnsVPNBytes_Type=Counter64
_SnsVPNBytes_Object=MibTableColumn
snsVPNBytes=_SnsVPNBytes_Object((1,3,6,1,4,1,11256,1,1,1,1,13),_SnsVPNBytes_Type())
snsVPNBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNBytes.setStatus(_A)
_SnsVPNMaxLifetime_Type=Counter64
_SnsVPNMaxLifetime_Object=MibTableColumn
snsVPNMaxLifetime=_SnsVPNMaxLifetime_Object((1,3,6,1,4,1,11256,1,1,1,1,14),_SnsVPNMaxLifetime_Type())
snsVPNMaxLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNMaxLifetime.setStatus(_A)
_SnsVPNMaxBytes_Type=Counter64
_SnsVPNMaxBytes_Object=MibTableColumn
snsVPNMaxBytes=_SnsVPNMaxBytes_Object((1,3,6,1,4,1,11256,1,1,1,1,15),_SnsVPNMaxBytes_Type())
snsVPNMaxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:snsVPNMaxBytes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsVPN':snsVPN,'snsVPNSATable':snsVPNSATable,'snsVPNSAEntry':snsVPNSAEntry,_E:snsVPNSAIndex,'snsVPNIPSrc':snsVPNIPSrc,'snsVPNIPDst':snsVPNIPDst,'snsVPNType':snsVPNType,'snsVPNMode':snsVPNMode,'snsVPNSpi':snsVPNSpi,'snsVPNPeerSpi':snsVPNPeerSpi,'snsVPNReqID':snsVPNReqID,'snsVPNEnc':snsVPNEnc,'snsVPNAuth':snsVPNAuth,'snsVPNState':snsVPNState,'snsVPNLifetime':snsVPNLifetime,'snsVPNBytes':snsVPNBytes,'snsVPNMaxLifetime':snsVPNMaxLifetime,'snsVPNMaxBytes':snsVPNMaxBytes})